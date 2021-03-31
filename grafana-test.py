
import collections
import requests

re = requests.get("http://atlas02.sigsus.cn/endpoints/grafana/api/datasources/proxy/1/api/v1/query_range?query=avg%20by(instance%2Cusername%2Cvc_name%"
                  "2Cdevice_type)%20(task_device_percent{username='715test'})&start=1592653500&end=1595245500&step=300",
                  headers={"Cookie":"token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjMwNTM4LCJ1c2VyTmFtZSI6Inl1bnhpYS5jaHUiLCJleHAiOjE1OTUzODI2MjcuNTUyLCJpYXQiOjE1OTUyMDk4Mjd9.EIcZaGENIEI75jwI5sBELVgvj-mP1PuT7IsArlz8R8I"})
met =re.json()["data"]["result"]
def walk_json_field_safe(obj, *fields):
    """ for example a=[{"a": {"b": 2}}]
    walk_json_field_safe(a, 0, "a", "b") will get 2
    walk_json_field_safe(a, 0, "not_exist") will get None
    """
    try:
        for f in fields:
            obj = obj[f]
        return obj
    except:
        return None
default = lambda : {"booked": collections.defaultdict(lambda : 0), "idle": collections.defaultdict(lambda : 0),"nonidle_util_sum": collections.defaultdict(lambda : 0.0),"nonidle_util":collections.defaultdict(lambda : 0.0)}
vc_level = collections.defaultdict(
    lambda: collections.defaultdict(default))
for metric in met:
    username = walk_json_field_safe(metric, "metric", "username")
    vc_name = walk_json_field_safe(metric, "metric", "vc_name")
    gpu_type = walk_json_field_safe(metric, "metric", "device_type")
    job_id = walk_json_field_safe(metric, "metric", "job_name")
    print(vc_name,gpu_type,job_id,metric["metric"])
    if username!="715test":
        continue
    values = metric["values"]
    su = 0
    for time, utils in values:
        if float(utils)<=0:
            su   += 300
    print(su)
    vc_level[vc_name][username]["idle"][gpu_type] += su
print(vc_level)
for i in range(1,1):
    print i
print([1,2][1:4])
with open("max_page","w") as f:
    f.write(str(2))