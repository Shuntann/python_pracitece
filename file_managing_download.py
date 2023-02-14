import shutil
import os

path1="C:\\Users\\SYUNTA\\Downloads"
path2="C:\\Users\\SYUNTA\\Documents\\留学"

#file_move=shutil.move(path1, path2)

#with open(path1) as f:
#   line = f.readlines()
#  print(line)
print("using os.listdir")
for name in os.listdir(path2):
    if os.path.isfile(name):
        print(f"file: {name}")
    else:
        print(f"dir: {name}")

print("using os.scandir")
for entry in os.scandir(path2):
    if entry.is_file():
        print(f"file: {entry.name}")
    else:
        print(f"dir: {entry.name}")

#os.makedirs("C:\\Users\\SYUNTA\\Documents\\python\\downloads\\textfiles")
#os.makedirs("C:\\Users\\SYUNTA\\Documents\\python\\downloads\\mp3files")
#os.makedirs("C:\\Users\\SYUNTA\\Documents\\python\\downloads\\pdfiles")
#os.makedirs("C:\\Users\\SYUNTA\\Documents\\python\\downloads\\exefiles")

text=".txt"; mp3=".mp3"; PDF=".pdf"; app=".exe"
file_name = ["textfiles", "mp3files", "pdfiles", "exefiles"]
path_4 = []
for name in file_name:
    path_4.append(os.path.join(path1, name))

#print(path_4) 確認用

extension_4 = [text, mp3, PDF, app]

d = {}

print("using: os.scandir")
for entry in os.scandir(path1):
    for extention_name, path_name in zip(extension_4, path_4):
        if entry.is_file():

            if entry.name[-4:] == extention_name:
                new = shutil.move(os.path.join(path1, entry.name),path_name)




#print("Q39")
#l1 = [1 ,2 ,3, 4, 5] 
#l2 = [10, 9, 8, 7, 6]
#new_list=[i*j for i, j in zip(l1, l2)]
#j=0
#for i in l1:
#    new_list.append(i*l2[j])
#    j+=1
