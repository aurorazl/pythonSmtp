import logging as logger
import collections
import math
from operator import add

def gen_vc_metrics(vc_info, vc_usage, cluster_gpu_info,cluster_npu_info,device_type_info):
    logger.info("vc_info %s, vc_usage %s, cluster_gpu_info %s cluster_npu_info %s device_type_info %s",
            vc_info, vc_usage, cluster_gpu_info,cluster_npu_info,device_type_info)

    try:
        vc_quota_sum = collections.defaultdict(lambda : 0)

        for vc_name, gpu_info in vc_info.items():
            for gpu_type, total in gpu_info.items():
                if gpu_type not in device_type_info:
                    continue
                vc_quota_sum[device_type_info[gpu_type]["deviceStr"]] += total

        unallocatable={}
        unallocatable["nvidia.com/gpu"] = cluster_gpu_info.capacity - cluster_gpu_info.allocatable
        unallocatable["npu.huawei.com/NPU"] = cluster_npu_info.capacity - cluster_npu_info.allocatable

        # key is vc_name, value is a map with key to be gpu_type and value to be real
        # quota
        ratio = collections.defaultdict(lambda : {})

        for vc_name, gpu_info in vc_info.items():
            for gpu_type, quota in gpu_info.items():
                if gpu_type not in device_type_info:
                    continue
                if vc_quota_sum[device_type_info[gpu_type]["deviceStr"]] == 0:
                    vc_quota = 0
                else:
                    vc_quota = quota - int(math.ceil(unallocatable[device_type_info[gpu_type]["deviceStr"]] * quota / vc_quota_sum[device_type_info[gpu_type]["deviceStr"]]))
                used = vc_usage.map[vc_name][gpu_type][1]
                preemptive_used = vc_usage.map[vc_name][gpu_type][0]

                ratio[vc_name][gpu_type] = [max(vc_quota - preemptive_used, 0),max(vc_quota - used, 0)]

        ratio_sum = collections.defaultdict(lambda : [0,0])
        for vc_name, gpu_info in ratio.items():
            for gpu_type, cur_ratio in gpu_info.items():
                if gpu_type not in device_type_info:
                    continue
                deviceStr = device_type_info[gpu_type]["deviceStr"]
                ratio_sum[deviceStr] = list(map(add,ratio_sum[deviceStr],cur_ratio))

        ### if not all devices is allcated to vc,this make sense
        for deviceStr,resources_list in ratio_sum.items():
            if deviceStr == "nvidia.com/gpu":
                cluster_info = cluster_gpu_info
            else:
                cluster_info = cluster_npu_info
            if resources_list[1]<cluster_info.available:
                resources_list[1] = cluster_info.available
            if resources_list[0] < cluster_info.preemptable_available:
                resources_list[0] = cluster_info.preemptable_available

        for vc_name, gpu_info in ratio.items():
            for gpu_type, cur_ratio in gpu_info.items():
                if gpu_type not in device_type_info:
                    continue
                if vc_name not in vc_usage.map or gpu_type not in vc_usage.map[vc_name]:
                    deviceStr = device_type_info[gpu_type]["deviceStr"]
                    labels = [vc_name, deviceStr]
                    # no job running in this vc or using this gpu type
                    if all((x== 0 for x in ratio_sum[deviceStr])):
                        available = 0
                        preemptive_available=0
                    else:
                        if deviceStr == "npu.huawei.com/NPU":
                            available = int(math.floor(cluster_npu_info.available * cur_ratio[1] / ratio_sum[deviceStr][1]))
                            reserved = int(math.floor(cluster_npu_info.reserved * cur_ratio[1] / ratio_sum[deviceStr][1]))
                            preemptive_available = int(math.floor(cluster_npu_info.preemptable_available * cur_ratio[0] / ratio_sum[deviceStr][0]))
                        else:
                            available = int(math.floor(cluster_gpu_info.available * cur_ratio[1] / ratio_sum[deviceStr][1]))
                            reserved = int(math.floor(cluster_gpu_info.reserved * cur_ratio[1] / ratio_sum[deviceStr][1]))
                            preemptive_available = int(math.floor(cluster_gpu_info.preemptable_available * cur_ratio[0] / ratio_sum[deviceStr][0]))
                    quota = vc_info[vc_name][gpu_type]
                    print(vc_name,gpu_type,available,reserved,preemptive_available)

        for vc_name, vc_usage_info in vc_usage.map.items():
            for gpu_type, vc_used in vc_usage_info.items():
                if gpu_type not in device_type_info:
                    continue
                if vc_name not in vc_info:
                    logger.warning("ignore used gpu in %s, but vc quota do not have this vc, possible due to job template error", vc_name)
                    continue

                if gpu_type not in vc_info[vc_name]:
                    logger.warning("ignore used gpu %s in %s, but vc quota do not have this gpu_type", gpu_type, vc_name)
                    continue
                deviceStr = device_type_info[gpu_type]["deviceStr"]
                labels = [vc_name, deviceStr]

                cur_ratio = ratio[vc_name][gpu_type]
                quota = vc_info[vc_name][gpu_type]
                if all((x== 0 for x in ratio_sum[deviceStr])):
                    available = 0
                    preemptive_available = 0
                    reserved = 0
                else:
                    if deviceStr == "npu.huawei.com/NPU":
                        available = int(math.floor(cluster_npu_info.available * cur_ratio[1] / ratio_sum[deviceStr][1]))
                        reserved = int(math.floor(cluster_npu_info.reserved * cur_ratio[1] / ratio_sum[deviceStr][1]))
                        preemptive_available = int(math.floor(cluster_npu_info.preemptable_available * cur_ratio[0] / ratio_sum[deviceStr][0])) if ratio_sum[deviceStr][0]!=0 else 0
                    else:
                        available = int(math.floor(cluster_gpu_info.available * cur_ratio[1] / ratio_sum[deviceStr][1]))
                        reserved = int(math.floor(cluster_gpu_info.reserved * cur_ratio[1] / ratio_sum[deviceStr][1]))
                        preemptive_available = int(math.floor(cluster_gpu_info.preemptable_available * cur_ratio[0] / ratio_sum[deviceStr][0])) if ratio_sum[deviceStr][0]!=0 else 0
                total_used, non_preemptable_used = vc_used
                print(vc_name,gpu_type,available, reserved, preemptive_available)
    except Exception as e:
        logger.exception("failed to process vc info")


class VcUsage(object):
    def __init__(self):
        # key is vc_name, value is a map with key to be gpu_type and value is an
        # array of two int.
        # The first is total used, the second is those non-preemptable used
        self.map = collections.defaultdict(lambda :
                collections.defaultdict(lambda : [0, 0]))
a = VcUsage()
a.map["platform"]["huawei_npu_arm64"]=[0,0]
a.map["vc2-4"]["huawei_npu_arm64"]=[2,2]
a.map["AscendVC"]["huawei_npu_arm64"]=[0,0]
a.map["TuringVC"]["huawei_npu_arm64"]=[2,2]
a.map["vc2-1"]["huawei_npu_arm64"]=[1,1]
a.map["vc2-3"]["huawei_npu_arm64"]=[1,1]
class ClusterGPUInfo(object):
    def __init__(self,capacity,available,preemptable_available,allocatable,reserved):
        self.capacity = capacity
        self.available = available
        self.preemptable_available = preemptable_available
        self.allocatable = allocatable
        self.reserved = reserved

re = gen_vc_metrics(
    {'vc2-4': {'huawei_npu_arm64': 2}, 'vc2-3': {'huawei_npu_arm64': 2}, 'vc2-2': {'huawei_npu_arm64': 2}, 'vc2-1': {'huawei_npu_arm64': 2}, 'platform': {'huawei_npu_arm64': 8}, 'AscendVC': {'huawei_npu_arm64': 4}, 'TuringVC': {'huawei_npu_arm64': 4}, 'vc8npu_new': {'huawei_npu_arm64': 8}}
               ,a,ClusterGPUInfo(0,0,0,0,0),ClusterGPUInfo(40,34,34,40,0),
               {'huawei_npu_arm64': {'capacity': 40, 'detail': [{'allocatable': 8, 'capacity': 8, 'nodeName': 'worker02'}, {'allocatable': 6, 'capacity': 8, 'nodeName': 'worker03'}, {'allocatable': 4, 'capacity': 8, 'nodeName': 'worker01'}, {'allocatable': 8, 'capacity': 8, 'nodeName': 'worker04'}, {'allocatable': 8, 'capacity': 8, 'nodeName': 'worker05'}], 'deviceStr': 'npu.huawei.com/NPU'}})


print(re)