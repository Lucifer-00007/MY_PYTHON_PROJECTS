#Sample prog to rename the file-list and move the files to a diff folder.
# This program is the updated_version of -- "Prog_To_Create_Folders_Acc_To_Given_Range.py"

# NOTE: This Program will create the "Folders" according to the "File_Range" and it will move the files to the created folders.


import os,shutil,time
print("Now moving the files...")
time.sleep(1)


Source_path=input("Enter The Path Of The Target Files =")


Target_path=input("Enter The Path Of The Target Folder =")

Subfolders_Name = [f.name for f in os.scandir(Target_path) if f.is_dir()]      #Here we will get the list of "name of subfolders".
subfolders_Path = [f.path for f in os.scandir(Target_path) if f.is_dir()]     #Here we will get the list of "path of the subfolders"
# print(*Subfolders_Name, sep="\n")

File_list_Name = [f.name for f in os.scandir(Source_path) if f.is_file()]      #Here we are getting new list of File
File_list_Path = [f.path for f in os.scandir(Source_path) if f.is_file()]     #Here we will get the list of "path of the Files"
# print(*File_list_Name, sep="\n")
# print(*File_list_Path, sep="\n")


for i in range(len(Subfolders_Name)):			  #Here we are iterrating the loop for number of time 'the no. of elements in list'.
	Split1 = Subfolders_Name[i].split("-")       #Here we split each string of the list(ie, 'File_list') by " given Tag1 "
	for k in range(len(File_list_Name)):	    #Here we are iterrating the loop for number of time 'the no. of elements in list'.
		Split2 = File_list_Name[k].split(".")
		if Split2[0]>=Split1[0] and Split2[0]<=Split1[1]:
			shutil.move(File_list_Path[k],subfolders_Path[i])

print(f"\nCongratulations!! Your Files Have Been Moved..!! \n\nFrom:- [{Source_path}] \n\nTo:- [{Target_path}]")



















