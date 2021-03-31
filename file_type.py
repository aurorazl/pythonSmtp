import mimetypes,filetype
print(mimetypes.guess_type("timg.mp4"))
mime = filetype.guess("test.jpg")
print(mime,dir(mime))
print(mime.MIME)

# import magic
# print(magic.from_file("timg.mp4"))

import os,re
import zipfile
a = zipfile.ZipFile("./test.zip",mode="r")
print(dir(a))
print(a.namelist())
print(a.extractall(path="./test1"))
import shutil
shutil.rmtree("./test1")
print([""]+["a","b"])
import os
for i in os.listdir("d:/apulis"):
    print(i,os.path.isfile(os.path.join("d:/apulis",i)))
print([ i for i in os.listdir("d:/apulis") if os.path.isfile(i)])
print("COCO".lower())
print("COCO%201.0".split("\\"))

print(filetype.guess("./meeting.jpg"))
print(filetype.guess("./config.c"))
import glob
print(list(glob.glob("./test") ))
print("./test/Documents/示例.jpg")
print(filetype.guess("/workstate/cvat/data/data/8/raw/annotations/cat_0.jpg"))
print(os.path.exists("/workstate/cvat/data/data/8/raw/annotations/cat_0.jpg"))
print(os.path.islink("/workstate/cvat/data/data/8/raw/annotations/cat_0.jpg"))