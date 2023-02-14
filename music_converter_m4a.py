import os
import shutil
import file_fomula
from pprint import pprint

download_path = "C:\\Users\\SYUNTA\\Downloads"
new_path = "D:\\Music"

path = "D:\\Music"

li =[]

if len(os.listdir(download_path)) >= 1:
    file_fomula.FileAndDir_Name(download_path)
    print(str(len(os.listdir(download_path))) + "個")

    for file_music in os.scandir(download_path):
        if file_music.name[-3:] == "mp3":

            file_fomula.file_moving(download_path, new_path, file_music.name)

            i = os.path.join(new_path, file_music.name)

            print(file_music.name)
            li.append(file_music.name)

            os.rename(i, i[:-3]+ "m4a")

            



else:
    print("no file in Download")

pprint(len(li))
pprint(li)
