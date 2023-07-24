import os
from os.path import join, getsize
for root, dirs, files in os.walk('D:\DevSecOps\Python\Final Project'):
    print(root, "consume", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
