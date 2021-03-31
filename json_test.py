a = {
    "mask-rcnn-inception-resnet-v2-atrous-coco": {
        "metadata": {"name": "mask-rcnn-inception-resnet-v2-atrous-coco", "namespace": "nuclio",
                     "labels": {"nuclio.io/project-name": "cvat"},
                     "annotations": {"framework": "openvino", "name": "Mask RCNN",
                                     "spec": "[\n  { \"id\": 1, \"name\": \"person\" },\n  { \"id\": 2, \"name\": \"bicycle\" },\n  { \"id\": 3, \"name\": \"car\" },\n  { \"id\": 4, \"name\": \"motorcycle\" },\n  { \"id\": 5, \"name\": \"airplane\" },\n  { \"id\": 6, \"name\": \"bus\" },\n  { \"id\": 7, \"name\": \"train\" },\n  { \"id\": 8, \"name\": \"truck\" },\n  { \"id\": 9, \"name\": \"boat\" },\n  { \"id\":10, \"name\": \"traffic_light\" },\n  { \"id\":11, \"name\": \"fire_hydrant\" },\n  { \"id\":13, \"name\": \"stop_sign\" },\n  { \"id\":14, \"name\": \"parking_meter\" },\n  { \"id\":15, \"name\": \"bench\" },\n  { \"id\":16, \"name\": \"bird\" },\n  { \"id\":17, \"name\": \"cat\" },\n  { \"id\":18, \"name\": \"dog\" },\n  { \"id\":19, \"name\": \"horse\" },\n  { \"id\":20, \"name\": \"sheep\" },\n  { \"id\":21, \"name\": \"cow\" },\n  { \"id\":22, \"name\": \"elephant\" },\n  { \"id\":23, \"name\": \"bear\" },\n  { \"id\":24, \"name\": \"zebra\" },\n  { \"id\":25, \"name\": \"giraffe\" },\n  { \"id\":27, \"name\": \"backpack\" },\n  { \"id\":28, \"name\": \"umbrella\" },\n  { \"id\":31, \"name\": \"handbag\" },\n  { \"id\":32, \"name\": \"tie\" },\n  { \"id\":33, \"name\": \"suitcase\" },\n  { \"id\":34, \"name\": \"frisbee\" },\n  { \"id\":35, \"name\": \"skis\" },\n  { \"id\":36, \"name\": \"snowboard\" },\n  { \"id\":37, \"name\": \"sports_ball\" },\n  { \"id\":38, \"name\": \"kite\" },\n  { \"id\":39, \"name\": \"baseball_bat\" },\n  { \"id\":40, \"name\": \"baseball_glove\" },\n  { \"id\":41, \"name\": \"skateboard\" },\n  { \"id\":42, \"name\": \"surfboard\" },\n  { \"id\":43, \"name\": \"tennis_racket\" },\n  { \"id\":44, \"name\": \"bottle\" },\n  { \"id\":46, \"name\": \"wine_glass\" },\n  { \"id\":47, \"name\": \"cup\" },\n  { \"id\":48, \"name\": \"fork\" },\n  { \"id\":49, \"name\": \"knife\" },\n  { \"id\":50, \"name\": \"spoon\" },\n  { \"id\":51, \"name\": \"bowl\" },\n  { \"id\":52, \"name\": \"banana\" },\n  { \"id\":53, \"name\": \"apple\" },\n  { \"id\":54, \"name\": \"sandwich\" },\n  { \"id\":55, \"name\": \"orange\" },\n  { \"id\":56, \"name\": \"broccoli\" },\n  { \"id\":57, \"name\": \"carrot\" },\n  { \"id\":58, \"name\": \"hot_dog\" },\n  { \"id\":59, \"name\": \"pizza\" },\n  { \"id\":60, \"name\": \"donut\" },\n  { \"id\":61, \"name\": \"cake\" },\n  { \"id\":62, \"name\": \"chair\" },\n  { \"id\":63, \"name\": \"couch\" },\n  { \"id\":64, \"name\": \"potted_plant\" },\n  { \"id\":65, \"name\": \"bed\" },\n  { \"id\":67, \"name\": \"dining_table\" },\n  { \"id\":70, \"name\": \"toilet\" },\n  { \"id\":72, \"name\": \"tv\" },\n  { \"id\":73, \"name\": \"laptop\" },\n  { \"id\":74, \"name\": \"mouse\" },\n  { \"id\":75, \"name\": \"remote\" },\n  { \"id\":76, \"name\": \"keyboard\" },\n  { \"id\":77, \"name\": \"cell_phone\" },\n  { \"id\":78, \"name\": \"microwave\" },\n  { \"id\":79, \"name\": \"oven\" },\n  { \"id\":80, \"name\": \"toaster\" },\n  { \"id\":81, \"name\": \"sink\" },\n  { \"id\":83, \"name\": \"refrigerator\" },\n  { \"id\":84, \"name\": \"book\" },\n  { \"id\":85, \"name\": \"clock\" },\n  { \"id\":86, \"name\": \"vase\" },\n  { \"id\":87, \"name\": \"scissors\" },\n  { \"id\":88, \"name\": \"teddy_bear\" },\n  { \"id\":89, \"name\": \"hair_drier\" },\n  { \"id\":90, \"name\": \"toothbrush\" }\n]\n",
                                     "type": "detector"}, "resourceVersion": "19647"},
        "spec": {"description": "Mask RCNN inception resnet v2 COCO via Intel OpenVINO", "handler": "main:handler",
                 "runtime": "python:3.6",
                 "env": [{"name": "NUCLIO_PYTHON_EXE_PATH", "value": "/opt/nuclio/common/python3"}], "resources": {},
                 "image": "harbor.sigsus.cn:8443/sz_gongdianju/cvat/openvino.omz.public.mask_rcnn_inception_resnet_v2_atrous_coco",
                 "imageHash": "1606132156543415284", "targetCPU": 75, "triggers": {
                "myHttpTrigger": {"class": "", "kind": "http", "name": "", "maxWorkers": 2,
                                  "workerAvailabilityTimeoutMilliseconds": 10000,
                                  "attributes": {"maxRequestBodySize": 33554432, "serviceType": "ClusterIP"}}},
                 "volumes": [
                     {"volume": {"name": "volume-1", "hostPath": {"path": "/root/cvat/serverless/openvino/common"}},
                      "volumeMount": {"name": "volume-1", "mountPath": "/opt/nuclio/common"}}], "version": -1,
                 "alias": "latest", "build": {
                "functionConfigPath": "/root/cvat/serverless/openvino/omz/public/mask_rcnn_inception_resnet_v2_atrous_coco/nuclio/function.yaml"},
                 "platform": {"attributes": {"restartPolicy": {"maximumRetryCount": 3, "name": "always"}}},
                 "readinessTimeoutSeconds": 60, "eventTimeout": "60s"}, "status": {"state": "ready", "logs": [
            {"level": "info", "message": "Deploying function", "name": "mask-rcnn-inception-resnet-v2-atrous-coco",
             "time": 1606132156540.0115},
            {"level": "info", "message": "Skipping build", "name": "mask-rcnn-inception-resnet-v2-atrous-coco",
             "time": 1606132156540.0444},
            {"functionName": "", "httpPort": 0, "level": "info", "message": "Function deploy complete",
             "name": "deployer", "time": 1606132191309.843}], "scaleToZero": {"lastScaleEvent": "resourceUpdated",
                                                                              "lastScaleEventTime": "2020-11-23T11:49:51.064078608Z"}}},
    "openvino-dextr": {
        "metadata": {"name": "openvino-dextr", "namespace": "nuclio", "labels": {"nuclio.io/project-name": "cvat"},
                     "annotations": {"framework": "openvino", "min_pos_points": "4", "name": "DEXTR", "spec": "",
                                     "type": "interactor"}, "resourceVersion": "19953"},
        "spec": {"description": "Deep Extreme Cut", "handler": "main:handler", "runtime": "python:3.6",
                 "env": [{"name": "NUCLIO_PYTHON_EXE_PATH", "value": "/opt/nuclio/common/python3"}], "resources": {},
                 "image": "harbor.sigsus.cn:8443/sz_gongdianju/cvat/openvino.dextr", "imageHash": "1606132216065412199",
                 "targetCPU": 75, "triggers": {
                "myHttpTrigger": {"class": "", "kind": "http", "name": "", "maxWorkers": 2,
                                  "workerAvailabilityTimeoutMilliseconds": 10000,
                                  "attributes": {"maxRequestBodySize": 33554432, "serviceType": "ClusterIP"}}},
                 "volumes": [
                     {"volume": {"name": "volume-1", "hostPath": {"path": "/root/cvat/serverless/openvino/common"}},
                      "volumeMount": {"name": "volume-1", "mountPath": "/opt/nuclio/common"}}], "version": -1,
                 "alias": "latest",
                 "build": {"functionConfigPath": "/root/cvat/serverless/openvino/dextr/nuclio/function.yaml"},
                 "platform": {"attributes": {"restartPolicy": {"maximumRetryCount": 3, "name": "always"}}},
                 "readinessTimeoutSeconds": 60, "eventTimeout": "30s"}, "status": {"state": "ready", "logs": [
            {"level": "info", "message": "Deploying function", "name": "openvino-dextr", "time": 1606132216062.9558},
            {"level": "info", "message": "Skipping build", "name": "openvino-dextr", "time": 1606132216062.9883},
            {"functionName": "", "httpPort": 0, "level": "info", "message": "Function deploy complete",
             "name": "deployer", "time": 1606132228095.9}], "scaleToZero": {"lastScaleEvent": "resourceUpdated",
                                                                            "lastScaleEventTime": "2020-11-23T11:50:27.966975494Z"}}},
    "person-reidentification-retail-0300": {
        "metadata": {"name": "person-reidentification-retail-0300", "namespace": "nuclio",
                     "labels": {"nuclio.io/project-name": "cvat"},
                     "annotations": {"framework": "openvino", "name": "Person reidentification", "spec": "",
                                     "type": "reid"}, "resourceVersion": "19884"},
        "spec": {"description": "Person reidentification model for a general scenario", "handler": "main:handler",
                 "runtime": "python:3.6",
                 "env": [{"name": "NUCLIO_PYTHON_EXE_PATH", "value": "/opt/nuclio/common/python3"}], "resources": {},
                 "image": "harbor.sigsus.cn:8443/sz_gongdianju/cvat/openvino.omz.intel.person-reidentification-retail-0300",
                 "imageHash": "1606132209620415987", "targetCPU": 75, "triggers": {
                "myHttpTrigger": {"class": "", "kind": "http", "name": "", "maxWorkers": 2,
                                  "workerAvailabilityTimeoutMilliseconds": 10000,
                                  "attributes": {"maxRequestBodySize": 33554432, "serviceType": "ClusterIP"}}},
                 "volumes": [
                     {"volume": {"name": "volume-1", "hostPath": {"path": "/root/cvat/serverless/openvino/common"}},
                      "volumeMount": {"name": "volume-1", "mountPath": "/opt/nuclio/common"}}], "version": -1,
                 "alias": "latest", "build": {
                "functionConfigPath": "/root/cvat/serverless/openvino/omz/intel/person-reidentification-retail-300/nuclio/function.yaml"},
                 "platform": {"attributes": {"restartPolicy": {"maximumRetryCount": 3, "name": "always"}}},
                 "readinessTimeoutSeconds": 60, "eventTimeout": "30s"}, "status": {"state": "ready", "logs": [
            {"level": "info", "message": "Deploying function", "name": "person-reidentification-retail-0300",
             "time": 1606132209617.8376},
            {"level": "info", "message": "Skipping build", "name": "person-reidentification-retail-0300",
             "time": 1606132209617.8955},
            {"functionName": "", "httpPort": 0, "level": "info", "message": "Function deploy complete",
             "name": "deployer", "time": 1606132215647.9163}], "scaleToZero": {"lastScaleEvent": "resourceUpdated",
                                                                               "lastScaleEventTime": "2020-11-23T11:50:15.46327709Z"}}},
    "siammask": {"metadata": {"name": "siammask", "namespace": "nuclio", "labels": {"nuclio.io/project-name": "cvat"},
                              "annotations": {"framework": "pytorch", "name": "SiamMask", "spec": "",
                                              "type": "tracker"}, "resourceVersion": "20273"},
                 "spec": {"description": "Fast Online Object Tracking and Segmentation", "handler": "main:handler",
                          "runtime": "python:3.6", "env": [{"name": "PYTHONPATH",
                                                            "value": "/opt/nuclio/SiamMask:/opt/nuclio/SiamMask/experiments/siammask_sharp"}],
                          "resources": {}, "image": "harbor.sigsus.cn:8443/sz_gongdianju/cvat/pth.foolwood.siammask",
                          "imageHash": "1606132318522846265", "targetCPU": 75, "triggers": {
                         "myHttpTrigger": {"class": "", "kind": "http", "name": "", "maxWorkers": 2,
                                           "workerAvailabilityTimeoutMilliseconds": 10000,
                                           "attributes": {"maxRequestBodySize": 33554432, "serviceType": "ClusterIP"}}},
                          "version": -1, "alias": "latest", "build": {
                         "functionConfigPath": "/root/cvat/serverless/pytorch/foolwood/siammask/nuclio/function.yaml"},
                          "platform": {"attributes": {"restartPolicy": {"maximumRetryCount": 3, "name": "always"}}},
                          "readinessTimeoutSeconds": 60, "eventTimeout": "30s"}, "status": {"state": "ready", "logs": [
            {"level": "info", "message": "Deploying function", "name": "siammask", "time": 1606132318519.7766},
            {"level": "info", "message": "Skipping build", "name": "siammask", "time": 1606132318519.8303},
            {"functionName": "", "httpPort": 0, "level": "info", "message": "Function deploy complete",
             "name": "deployer", "time": 1606132330552.2522}], "scaleToZero": {"lastScaleEvent": "resourceUpdated",
                                                                               "lastScaleEventTime": "2020-11-23T11:52:10.410350935Z"}}},
    "text-detection-0004": {
        "metadata": {"name": "text-detection-0004", "namespace": "nuclio", "labels": {"nuclio.io/project-name": "cvat"},
                     "annotations": {"framework": "openvino", "name": "Text detection v4",
                                     "spec": "[\n  { \"id\": 1, \"name\": \"text\" }\n]\n", "type": "detector"},
                     "resourceVersion": "19766"},
        "spec": {
            "description": "Text detector based on PixelLink architecture with MobileNetV2-like as a backbone for indoor/outdoor scenes.",
            "handler": "main:handler", "runtime": "python:3.6",
            "env": [{"name": "NUCLIO_PYTHON_EXE_PATH", "value": "/opt/nuclio/common/python3"}], "resources": {},
            "image": "harbor.sigsus.cn:8443/sz_gongdianju/cvat/openvino.omz.intel.text-detection-0004",
            "imageHash": "1606132198621264498", "targetCPU": 75, "triggers": {
                "myHttpTrigger": {"class": "", "kind": "http", "name": "", "maxWorkers": 2,
                                  "workerAvailabilityTimeoutMilliseconds": 10000,
                                  "attributes": {"maxRequestBodySize": 33554432, "serviceType": "ClusterIP"}}},
            "volumes": [{"volume": {"name": "volume-1", "hostPath": {"path": "/root/cvat/serverless/openvino/common"}},
                         "volumeMount": {"name": "volume-1", "mountPath": "/opt/nuclio/common"}}], "version": -1,
            "alias": "latest", "build": {
                "functionConfigPath": "/root/cvat/serverless/openvino/omz/intel/text-detection-0004/nuclio/function.yaml"},
            "platform": {"attributes": {"restartPolicy": {"maximumRetryCount": 3, "name": "always"}}},
            "readinessTimeoutSeconds": 60, "eventTimeout": "30s"},
        "status": {"state": "ready", "logs": [
            {"level": "info", "message": "Deploying function", "name": "text-detection-0004",
             "time": 1606132198618.425},
            {"level": "info", "message": "Skipping build", "name": "text-detection-0004", "time": 1606132198618.4727},
            {"functionName": "", "httpPort": 0, "level": "info", "message": "Function deploy complete",
             "name": "deployer", "time": 1606132202640.6262}], "scaleToZero": {"lastScaleEvent": "resourceUpdated",
                                                                               "lastScaleEventTime": "2020-11-23T11:50:02.432873318Z"}}}
}
