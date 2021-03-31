import argparse
import textwrap
import numpy as np
import requests
import re
import json
import collections

from itertools import chain

import requests
# a = {"filename":"test/api/nfs/public/demo/testmap/test.json","data":"z"*1024*1024*15}
# res = requests.post("https://apulis-test.sigsus1.cn:51444/data_platform/api/image/UploadGeoJson",json=[a],verify=False)
# print(res.status_code,res.content)

from jinja2 import Environment, FileSystemLoader, Template
ENV_local = Environment(loader=FileSystemLoader("."))
template = ENV_local.get_template("./test.env")
content = template.render(cnf={"inference":{"tensorflow":[{"version":"12@asd","image":"gg"},{"version":"12","image":None}],"pytorch":[]},"gpuType":None})
with open("test.out", 'wb') as f:
    f.write(content.encode('utf-8'))
import yaml
f = open("test.out")
config = yaml.load(f)
print(config["inference"])
import datetime
now = datetime.datetime.now()
delta = datetime.timedelta(days=31)
one_month_ago = int(datetime.datetime.timestamp(now - delta))
print(int(datetime.datetime.timestamp(now)))
print(one_month_ago)