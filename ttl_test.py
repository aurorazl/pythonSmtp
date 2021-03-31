from cachetools import cached, TTLCache
vc_cache = TTLCache(maxsize=10240, ttl=12)
vc_cache[1]=1
print(1 in vc_cache)
# print(vc_cache[2])

import os
# print(os.getuid())
# print(os.path.isdir("/tmp/apachectl"))
# print(os.listdir("/tmp/'mod_wsgi-localhost:8001:0'\\handler.wsgi"))


# from urllib import request as urlrequest
# url = "https://avatars0.githubusercontent.com/u/13832349?s=60&v=4"
# req = urlrequest.Request(url, headers={'User-Agent': 'Mozilla/5.0'},unverifiable=True)
# print(urlrequest.urlopen(req))

import time
print(time.strftime("%y%m%d"))