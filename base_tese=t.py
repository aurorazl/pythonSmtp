import base64
import yaml
import json
import time
import math
print(base64.b64encode(str(30834).encode()))
print(base64.b64decode("NDMzNDc="))
print(json.dumps(["asd","asd"]))
print(None in [None])
print(time.time())
a = slice(1,2)
print([1,1,3][a])
print(math.ceil(0.1))
import datetime
print( time.mktime(datetime.datetime(2020, 7, 13, 13, 0, 14).timetuple()))