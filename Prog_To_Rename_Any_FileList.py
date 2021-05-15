# In this program we will rename all File in a directory to its "desired slice out name" from its initial name.
# Eg.  If Initial_name="AnimePahe1_Detective_Conan_-_460_396p_DCTP.mp4 - Copy (2) - Copy.txt"  ,
#      Split1="_-_"  ,  Split2="_396p" and File_extension=".txt" ,
#  	   then  Final_name="460.txt"   
 



# #Type1, Basic prog:-
# import os
#  New_dir=os.chdir(input("Enter your path here ="))                     #Here we are taking the 'path from the user' where we have to rename the files.
# print("\nThis is the new 'current working dir' =",[ os.getcwd() ])      #Here we print the 'new given path'..

# spt1=input("Enter the 'char' or 'string' just before the required name =")
# spt2=input("Enter the 'char' or 'string' just after the required name =")
# fextension=input("Enter the file extension here with a '.' =")
# File_list=os.listdir(New_dir)           #Here we are getting list of File-Folder

# for i in range(len(File_list)):         #Here we are iterrating the loop for number of time 'the no. of elements in list'.
#     Split1 = File_list[i].split(spt1)   #Here we split each string of the list(ie, 'File_list') by "_-_"
#     Split2 = Split1[1].split(spt2)[0]   #Here we split each string of 'Split1[1]'(ie, second-part[1] of  the strings of Split1) by "_" and store the first part of the string(ie. [0] in Split2)
#     d=f"{Split2}{fextension}"
#     # print(d)
#     os.rename(File_list[i],d)          #Here we rename the file as "os.rename(initial_name,final_name)"

# print("Congratulations!! The file-names are chaged!!")


# #Type 2:-
# import test1234
# import os
# # New_dir=os.chdir(input("Enter your path here ="))                     #Here we are taking the 'path from the user' where we have to rename the files.
# print("\nThis is the new 'current working dir' =",[ os.getcwd() ])      #Here we print the 'new given path'..
#
# spt1=input("Enter the 'char' or 'string' just before the required name =")
# spt2=input("Enter the 'char' or 'string' just after the required name =")
# fextension=input("Enter the file extension here with a '.' =")
# File_list=os.listdir(New_dir)           #Here we are getting list of File-Folder
#
# mn=test1234.ff
# if mn==1:
#     for i in range(len(File_list)):         #Here we are iterrating the loop for number of time 'the no. of elements in list'.
#         Split1 = File_list[i].split(spt1)   #Here we split each string of the list(ie, 'File_list') by "_-_"
#         Split2 = Split1[1].split(spt2)[0]   #Here we split each string of 'Split1[1]'(ie, second-part[1] of  the strings of Split1) by "_" and store the first part of the string(ie. [0] in Split2)
#         d=f"{Split2}{fextension}"
#         # print(d)
#         os.rename(File_list[i],d)          #Here we rename the file as "os.rename(initial_name,final_name)"
#
#     print("Congratulations!! The file-names are chaged!!")
# else:
#     pass



# Type3, Errors fixed:-
import os
Your_path=os.chdir(input("Enter your path here ="))               #Here we are taking the 'path from the user' where we have to rename the files.
print("\nThis is the new working dir =",[ os.getcwd() ])      #Here we print the 'new given path'..

Tag1=input("Enter the 'char' or 'string' just before the required name =")
Tag2=input("Enter the 'char' or 'string' just after the required name =")
fextension=input("Enter the file extension here with a '.' =")
# File_list=os.listdir(Your_path)           #Here we are getting list of File-Folder

File_list = [f.name for f in os.scandir(Your_path) if f.is_file()]    #Here we are getting list of File


#----------------------If You Want To Rename The Filelist To It's First Name----------------------#
if Tag1== "":
	for i in range(len(File_list)):           #Here we are iterrating the loop for number of time 'the no. of elements in list'.
		Split1 = File_list[i].split(Tag2)[0]
		d=f"{Split1}{fextension}"
		# d=f"{601+i}{fextension}"            #To rename the files to ascending number series(Here "600" can be replaced by "any required number")
		# print(d)
		os.rename(File_list[i],d)            #Here we rename the file as "os.rename(initial_name,final_name)"


#----------------------If You Want to Rename The Filelist To It's Last Name----------------------#
elif Tag2== "":
	for i in range(len(File_list)):         #Here we are iterrating the loop for number of time 'the no. of elements in list'.
		Split1 = File_list[i].split(Tag1)[1]
		d=f"{Split1}"
		# print(d)
		os.rename(File_list[i],d)          #Here we rename the file as "os.rename(initial_name,final_name)"


#----------------------If You Want to Rename The Filelist To a particular string/character/number----------------------#
else:
	for i in range(len(File_list)):			#Here we are iterrating the loop for number of time 'the no. of elements in list'.
		Split1 = File_list[i].split(Tag1)   #Here we split each string of the list(ie, 'File_list') by " given Tag1 "
		Split2 = Split1[1].split(Tag2)[0]   #Here we split each string of 'Split1[1]'(ie, second-part[1] of  the strings of Split1) by " given Tag2 " and store the first part of the string(ie. [0] in Split2)
		d=f"{Split2}{fextension}"
		# print(d)
		os.rename(File_list[i],d)          #Here we rename the file as "os.rename(initial_name,final_name)"


print("\nCongratulations!! The file-names are chaged!!")

New_File_list = [f.name for f in os.scandir(Your_path) if f.is_file()]      #Here we are getting new list of File

#----------------------Printing Initial and Finall filename list----------------------#
print("\nThis was the inital namelist of files =")
print(*File_list, sep="\n")
print("\nThis is the new namelist of files =")
print(*New_File_list, sep="\n")



