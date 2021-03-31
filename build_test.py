a = [1]
a = a*10
print(a)
import pickle
import uuid
print(uuid.uuid4())
print({"s":1}.update({"a":2}))

from pyunpack import Archive
import zipfile
import os
# Archive("d:/workstate/cvat/data/data/8/raw/Documents.rar").extractall("./test")
print("D:\\\\workstate\\\\cvat\\\\tmp\\\\cvat_312z27y5g'\n".split("cvat_"))
_zip_source = zipfile.ZipFile(r"C:\Users\DELL\Documents\WXWork\1688850723373906\Cache\File\2020-12\图片.zip", mode='r')
print(_zip_source.namelist()[0].encode("cp437").decode("gbk"))
_zip_source.read(_zip_source.namelist()[0].encode("cp437").decode("gbk").encode("gbk").decode("cp437"))
os.environ["PYTHONIOENCODING"]="utf-8"
import sys,locale
print(sys.stdin.encoding)
print(locale.getpreferredencoding())
_zip_source.extractall(path="./test")
print(_zip_source)