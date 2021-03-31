# -*- coding: utf-8 -*-
a = "2020-08-04T01:59:26"
import time
import datetime
# print(time.strftime("%Y-%m-%d",datetime.datetime.strptime(a,"%Y-%m-%dT%H:%M:%SZ").timetuple()))
# print(datetime.datetime.strptime(a,"%Y-%m-%dT%H:%M:%S").timestamp())
import pytz
import collections
date = datetime.datetime.now()
print(date)
# date = datetime.datetime.strptime("date", "%Y-%m-%dT%H:%M:%SZ")
print(pytz.utc.localize(date).isoformat())
print(pytz.utc.localize(date))
print(type(pytz.utc.localize(date)))
import os
print(os.path.join("中文","test"),"{}.json".format("中文"))
a = collections.defaultdict(lambda :[])
a["s"] = 1
print(3600*24*30*12*10)
import requests
import json
re = requests.get("http://china-gpu02.sigsus.cn/apis/UpdateVC?vcName=platform&userName=admin&quota="+json.dumps({"nvidia_gpu_amd64":16})+"&metadata="+json.dumps({"nvidia_gpu_amd64":{"user_quota":16}}))
print(re.content)
a = set()
a.add("s")
print("s" in a)
a,b = "ss".split("-")
print(a,b)