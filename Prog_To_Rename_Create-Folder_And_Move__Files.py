#Sample program to rename the file-list, create folders and move the files to a diff folder.
# This program is the updated_version of -- "Prog_To_Sort_And_Move_Files_To_Folder.py"


#Type1:-
##----------------------------------------------Renaming-Files----------------------------------------------##
import os,shutil,time,math

Your_path=os.chdir(input("Enter Your Path To Rename Files ="))               #Here we are taking the 'path from the user' where we have to rename the files.

print("\nThis is the new working dir =",[ os.getcwd() ])      #Here we print the 'new given path'..

Tag1=input("Enter the 'char' or 'string' just before the required name =")
Tag2=input("Enter the 'char' or 'string' just after the required name =")
fextension=input("Enter the file extension here with a '.' =")

File_list = [f.name for f in os.scandir(Your_path) if f.is_file()]    #Here we are getting list of File



#----------------------If You Want To Rename The Filelist To It's First Name----------------------#
if Tag1== "":
	for i in range(len(File_list)):           #Here we are iterrating the loop for number of time 'the no. of elements in list'.
		Split1 = File_list[i].split(Tag2)[0]
		d=f"{Split1}{fextension}"
		# print(d)                            #This is for testing purpose
		os.rename(File_list[i],d)            #Here we rename the file as "os.rename(initial_name,final_name)"


#----------------------If You Want to Rename The Filelist To It's Last Name----------------------#
elif Tag2== "":
	for i in range(len(File_list)):         #Here we are iterrating the loop for number of time 'the no. of elements in list'.
		Split1 = File_list[i].split(Tag1)[1]
		d=f"{Split1}"
		# print(d)                          #This is for testing purpose
		os.rename(File_list[i],d)          #Here we rename the file as "os.rename(initial_name,final_name)"


#----------------------If You Want to Rename The Filelist To a particular string/character/number----------------------#
else:
	for i in range(len(File_list)):			#Here we are iterrating the loop for number of time 'the no. of elements in list'.
		Split1 = File_list[i].split(Tag1)   #Here we split each string of the list(ie, 'File_list') by " given Tag1 "
		Split2 = Split1[1].split(Tag2)[0]   #Here we split each string of 'Split1[1]'(ie, second-part[1] of  the strings of Split1) by " given Tag2 " and store the first part of the string(ie. [0] in Split2)
		d=f"{Split2}{fextension}"
		# print(d)                          #This is for testing purpose
		os.rename(File_list[i],d)          #Here we rename the file as "os.rename(initial_name,final_name)"


print("\nCongratulations!! The file-names are chaged!!")

New_File_list = [f.name for f in os.scandir(Your_path) if f.is_file()]      #Here we are getting new list of File

#----------------------Printing Initial and Finall filename list----------------------#
print("\nThis was the inital namelist of files =")
print(*File_list, sep="\n")
print("\nThis is the new namelist of files =")
print(*New_File_list, sep="\n")




##----------------------------------------------Creating-Folders----------------------------------------------##
print("\nNow Creating The Folders...")
time.sleep(1)

File_list_Name = [f.name for f in os.scandir(Your_path) if f.is_file()]      #Here we are getting new list of File
First_File=File_list_Name[0]
Last_file=File_list_Name[len(File_list_Name) - 1]

sp=int(First_File.split(".")[0])                               #Here we take the first-file-name(ie. starting number) from the user.
ep=int(Last_file.split(".")[0])                                #Here we take the last-file-name(ie. ending number) from the user.

frange=int(input("Enter The Range ="))                    #Here we take the "file-range" for the "folder-name that we are going to create".
# frange=5                                               #This is for testing purpose.
Path_Of_Folders=input("Enter Your Path Where You Have To Create The Folders =")       #Here we enter the path where we are going to create the folders.

my_iter=math.ceil((ep-sp+1)/frange)                    #Here we getting the "value of number of required folders".

print(f"\nThe New Folders at [{Path_Of_Folders}] are:-")

for i in range(my_iter):                       #Here we are iterating the loop according to the "number of required folders".
    n=sp+frange*i
    i=i+1
    k=n+frange-1
    print(f"[{n}-{k}]")                       #Printing the Created-folders-name.

    s=f"{n}-{k}"                              #Storing the folders name.
    os.chdir(Path_Of_Folders)                  #Changing the path to the location where we want to create the new folders.
    os.makedirs(s)                              #Finally creating the folders.



##----------------------------------------------Moving-Files-To-Folders----------------------------------------------##
print("\nNow moving the files...")
time.sleep(1)

Source_path=input("Enter The Path Of The Target Files For Moving =")

Subfolders_Name = [f.name for f in os.scandir(Path_Of_Folders) if f.is_dir()]      #Here we will get the list of "name of subfolders".
subfolders_Path = [f.path for f in os.scandir(Path_Of_Folders) if f.is_dir()]      #Here we will get the list of "path of the subfolders"
# print(*Subfolders_Name, sep="\n")                                                #This is for testing purpose


File_list_Name = [f.name for f in os.scandir(Source_path) if f.is_file()]      #Here we are getting new list of File
File_list_Path = [f.path for f in os.scandir(Source_path) if f.is_file()]      #Here we will get the list of "path of the Files"
# print(*File_list_Name, sep="\n")                                             #This is for testing purpose


for i in range(len(Subfolders_Name)):			  #Here we are iterrating the loop for number of time 'the no. of elements in list'.
	Split1 = Subfolders_Name[i].split("-")       #Here we split each string of the list(ie, 'File_list') by " given Tag1 "
	for k in range(len(File_list_Name)):	    #Here we are iterrating the loop for number of time 'the no. of elements in list'.
		Split2 = File_list_Name[k].split(".")
		if Split2[0]>=Split1[0] and Split2[0]<=Split1[1]:
			shutil.move(File_list_Path[k],subfolders_Path[i])

print(f"\nCongratulations!! Your Files Have Been Moved..!! \n\nFrom:- [{Source_path}] \n\nTo:- [{Path_Of_Folders}]")




#Type2:-
# ##----------------------------------------------Renaming-Files----------------------------------------------##
# import os,shutil,time,math
#
# # Your_path=os.chdir(input("Enter Your Path To Rename Files ="))           #Here we are taking the 'path from the user' where we have to rename the files.
# print("\nThis is the new working dir =",[ os.getcwd() ])               #Here we print the 'new given path'..
#
# # Tag1=input("Enter the 'char' or 'string' just before the required name =")
# Tag1="_-_"                           #This is for testing purpose
#
# # Tag2=input("Enter the 'char' or 'string' just after the required name =")
# Tag2="_"                             #This is for testing purpose
#
# # fextension=input("Enter the file extension here with a '.' =")
# fextension=".txt"                    #This is for testing purpose
#
# File_list = [f.name for f in os.scandir(Your_path) if f.is_file()]    #Here we are getting list of File only.
#
#
# #----------------------If You Want To Rename The Filelist To It's First Name----------------------#
# if Tag1== "":
# 	for i in range(len(File_list)):           #Here we are iterrating the loop for number of time 'the no. of elements in list'.
# 		Split1 = File_list[i].split(Tag2)[0]
# 		d=f"{Split1}{fextension}"
# 		# print(d)                            #This is for testing purpose
# 		os.rename(File_list[i],d)            #Here we rename the file as "os.rename(initial_name,final_name)"
#
#
# #----------------------If You Want to Rename The Filelist To It's Last Name----------------------#
# elif Tag2== "":
# 	for i in range(len(File_list)):         #Here we are iterrating the loop for number of time 'the no. of elements in list'.
# 		Split1 = File_list[i].split(Tag1)[1]
# 		d=f"{Split1}"
# 		# print(d)                          #This is for testing purpose.
# 		os.rename(File_list[i],d)          #Here we rename the file as "os.rename(initial_name,final_name)"
#
#
# #----------------------If You Want to Rename The Filelist To a particular string/character/number----------------------#
# else:
# 	for i in range(len(File_list)):			#Here we are iterrating the loop for number of time 'the no. of elements in list'.
# 		Split1 = File_list[i].split(Tag1)   #Here we split each string of the list(ie, 'File_list') by " given Tag1 "
# 		Split2 = Split1[1].split(Tag2)[0]   #Here we split each string of 'Split1[1]'(ie, second-part[1] of  the strings of Split1) by " given Tag2 " and store the first part of the string(ie. [0] in Split2)
# 		d=f"{Split2}{fextension}"
# 		# print(d)                          #This is for testing purpose.
# 		os.rename(File_list[i],d)          #Here we rename the file as "os.rename(initial_name,final_name)"
#
#
# print("\nCongratulations!! The file-names are chaged!!")
#
# New_File_list = [f.name for f in os.scandir(Your_path) if f.is_file()]      #Here we are getting new list of File
#
# #----------------------Printing Initial and Finall filename list----------------------#
# print("\nThis was the inital namelist of files =")
# print(*File_list, sep="\n")
# print("\nThis is the new namelist of files =")
# print(*New_File_list, sep="\n")
#
#
#
#
# ##----------------------------------------------Creating-Folders----------------------------------------------##
# print("\nNow Creating The Folders...")
# time.sleep(1)
#
# # File_list_Name = [f.name for f in os.scandir(Your_path) if f.is_file()]      #Here we are getting new list of File
# # First_File=File_list_Name[0]
# # Last_file=File_list_Name[len(File_list_Name) - 1]
#
# First_File=New_File_list[0]                              #This is for testing purpose.
# Last_file=New_File_list[len(New_File_list) - 1]              #This is for testing purpose.
#
#
# sp=int(First_File.split(".")[0])                               #Here we take the first-file-name(ie. starting number) from the user.
# ep=int(Last_file.split(".")[0])                                #Here we take the last-file-name(ie. ending number) from the user.
#
# # frange=int(input("Enter The Range ="))               #Here we take the "file-range" for the "folder-name that we are going to create".
# frange=5                                               #This is for testing purpose.
#
# # Path_Of_Folders=input("Enter Your Path Where You Have To Create The Folders =")       #Here we enter the path where we are going to create the folders.
#
# my_iter=math.ceil((ep-sp+1)/frange)                    #Here we getting the "value of number of required folders".
#
# print(f"\nThe New Folders at [{Path_Of_Folders}] are:-")
#
# for i in range(my_iter):                       #Here we are iterating the loop according to the "number of required folders".
#     n=sp+frange*i
#     i=i+1
#     k=n+frange-1
#     print(f"[{n}-{k}]")                       #Printing the Created-folders-name.
#
#     # s=f"{n}-{k}"                              #Storing the folders name.
#     # os.chdir(Path_Of_Folders)                  #Changing the path to the location where we want to create the new folders.
#     # os.makedirs(s)                              #Finally creating the folders.
#
#
#
# # ##----------------------------------------------Moving-Files-To-Folders----------------------------------------------##
# print("\nNow moving the files...")
# time.sleep(1)
#
# # Source_path=input("Enter The Path Of The Target Files For Moving =")
#
# Subfolders_Name = [f.name for f in os.scandir(Path_Of_Folders) if f.is_dir()]      #Here we will get the list of "name of subfolders".
# subfolders_Path = [f.path for f in os.scandir(Path_Of_Folders) if f.is_dir()]     #Here we will get the list of "path of the subfolders"
# # print(*Subfolders_Name, sep="\n")
#
#
# # File_list_Name = [f.name for f in os.scandir(Source_path) if f.is_file()]      #Here we are getting new list of File
# # File_list_Name = [f.name for f in os.scandir(Your_path) if f.is_file()]      #Here we are getting new list of File
# # File_list_Path = [f.path for f in os.scandir(Source_path) if f.is_file()]     #Here we will get the list of "path of the Files"
# File_list_Path = [f.path for f in os.scandir(Your_path) if f.is_file()]     #Here we will get the list of "path of the Files"
# # print("The File list are = ",*File_list_Path, sep="\n")                                            #This is for testing purpose.
#
#
# # for i in range(len(Subfolders_Name)):			  #Here we are iterrating the loop for number of time 'the no. of elements in list'.
# # 	Split1 = Subfolders_Name[i].split("-")       #Here we split each string of the list(ie, 'File_list') by " given Tag1 "
# # 	for k in range(len(New_File_list)):	    #Here we are iterrating the loop for number of time 'the no. of elements in list'.
# # 		Split2 = New_File_list[k].split(".")
# # 		if Split2[0]>=Split1[0] and Split2[0]<=Split1[1]:
# # 			shutil.move(File_list_Path[k],subfolders_Path[i])
#
# print(f"\nCongratulations!! Your Files Have Been Moved..!! \n\nFrom:- [{Your_path}] \n\nTo:- [{Path_Of_Folders}]")
# # print(f"\nCongratulations!! Your Files Have Been Moved..!! \n\nFrom:- [{Source_path}] \n\nTo:- [{Path_Of_Folders}]")




















