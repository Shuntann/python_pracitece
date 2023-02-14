import file_fomula
import os


path = str(input("Enter Path First:"))


file_fomula.judge_filexist(path)

file_fomula.FileAndDir_Name(path)

print(os.listdir(path))

x=file_fomula.Get_File_Path(path)
print(x)

New_Path = str(input("Enter New Path:"))

file_fomula.filemoving(x, New_Path)

