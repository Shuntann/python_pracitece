import os
import shutil
from pprint import pprint

path = "D:\\Music"

file_name = str(input("Enter name to analyze : "))


for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)):
        if file_name in i:

            print(path)
            print(i)
            print("File existed")

    elif os.path.isdir(os.path.join(path, i)):
        new_path = os.path.join(path, i)
        for ii in os.listdir(new_path):
            if file_name in ii:

                print(new_path)
                print(ii)
                print("File existed")


