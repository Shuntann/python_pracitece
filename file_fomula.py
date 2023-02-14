import os
import shutil
      

def judge_filexist(file_path):
    if len(os.listdir(file_path)) >= 1:
        print("start")
    else:
        print("no file or dir")

def FileAndDir_Name(path):
    for FDname in os.scandir(path):
        if FDname.is_file():
            print(f"file: {FDname.name}")
        else:
            print(f"dir:  {FDname.name}")

def Get_File_Path(DirPath):
    if len(os.listdir(DirPath)) >= 1:
        FileName = str(input("Enter file name. Or skip："))
        if FileName == "":
            return DirPath

        else:
            return os.path.join(DirPath, FileName)

    else:
        return "no file or dir"




def file_moving(c_path, new_path, f_name):

    for exist in os.listdir(new_path):
        if exist == f_name:
            os.remove(os.path.join(new_path, f_name))
            break

    new = shutil.move(os.path.join(c_path, f_name), new_path)

def find_samefile(d_path):

    l_dir = []
    l_file = []

    file_name = str(input("Enter name to analyse : "))

    for FinD_name in os.listdir(d_path):
        if file_name in FinD_name:
            print(FinD_name)
            print("File existed")

            break

        else:
            continue

    
    for i in os.listdir(d_path):
        if os.path.isfile(os.path.join(d_path, i)):
            print("ファイル")
            l_file.append(i)
        
        elif os.path.isdir(os.path.join(d_path, i)):
            print("ディレ")
            l_dir.append(i)
                    
    print(len(l_file))
    print(len(l_dir))