import yaml
with open("test.yaml","r") as f:
    output = f.read()
import json
import time
t1 = time.time()
deploys = json.loads(output)
print(time.time()-t1)
models = []

if "items" in deploys:
    for deploy in deploys["items"]:
        models.append({
            "description": deploy["metadata"]['annotations'].get('description', ""),
            "id": deploy["metadata"]['annotations'].get('id', ""),
            "kind": deploy["metadata"]['annotations'].get('type'),
            "labels": [item['name'] for item in json.loads(deploy['metadata']['annotations'].get('spec') or '[]')],
            "min_pos_points": int(deploy['metadata']['annotations'].get('min_pos_points', 1)),
            "name": deploy['metadata']['annotations'].get('name', deploy["metadata"]["name"]),
            "state": "ready" if deploy['status'].get('readyReplicas', 0) >= 1 else "error",
            "framework": deploy['metadata']['annotations'].get('framework'),
        })

print(time.time()-t1)