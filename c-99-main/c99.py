import os
import shutil
#os.system("date")
#os.mkdir("C:/Users/my pc/OneDrive/Documents/python/c99/test")
os.getcwd()
path="C:/Users/my pc/OneDrive/Documents/python/c99/test"
isExist= os.path.exists(path)
print(isExist)
root_ext= os.path.splitext(path)
print("root part",root_ext[0])
print("ext part", root_ext[1],"\n")
#path
print("before copying files:")
print(os.listdir(path))
source= "C:/Users/my pc/OneDrive/Documents/python/c99/test/test.txt"
destination= "C:/Users/my pc/OneDrive/Documents/python/c99/test/test1.txt"
dest= shutil.copy(source,destination)
print("after copying files")
print(os.listdir(path))
print("before moving files")
print(os.listdir(path))
source1= "C:/Users/my pc/OneDrive/Documents/python/c99/test/mp4"
destination1= "C:/Users/my pc/OneDrive/Documents/python/c99/test/png"
dest1= shutil.move(source1,destination1)
print("after moving files")
print(os.listdir(path))


