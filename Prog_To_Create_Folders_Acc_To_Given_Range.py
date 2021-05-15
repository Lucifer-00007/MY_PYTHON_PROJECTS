#Program to create folders according to a given range to sort files in folder.
#Eg.  If we have some '.txt' files like: "1.txt, 2.txt, 3.txt ......n.txt".
# 	  Now we want "file_range=5", ie. we will create a folder name '1-5' and in this '1-5' folder will contain "1.txt, 2.txt, 3.txt, 4.txt, 5.txt" ,
#     Similarly '6-10' folder will contain "6.txt, 7.txt, 8.txt, 9.txt, 10.txt" and so on..
#     In this way this program will make a set of 5(file_range) files and separate them in a folder.
#     It will continue this process until all files are separated in folders.
#
# NOTE: This Program will only create the "Folders" according to the "File_Range" but it will not move the files to the created folders.	



# #Type1:-
# import math,os
#
# # sp=int(input("Enter The_First_File_Name ="))      #Here we take the first-file-name(ie. starting number and "By-Default it's = 1") from the user.
# ep=int(input("Enter The_Last_File_Name ="))        #Here we take the last-file-name(ie. ending number) from the user.
# # ep=100                                                #This is for testing purpose.
# frange=int(input("Enter The Range ="))               #Here we take the "file-range" for the "folder-name that we are going to create".
# # frange=10                                               #This is for testing purpose.
# Path_Of_Folders=input("Enter Your Path Here =")        #Here we enter the path where we are going to create the folders.
#
# my_iter=math.ceil(ep/frange)                    #Here we getting the "value of number of required folders".
#
# print(f"\nThe New Folders at [{Path_Of_Folders}] are:-")
# for i in range(my_iter):                       #Here we are iterating the loop according to the "number of required folders".
#     n=i*frange+1
#     i=i+1
#     k=i*frange
#     print(f"[{n}-{k}]")                       #Printing the Created-folders-name.
#
#     s=f"{n}-{k}"                              #Storing the folders name.
#     os.chdir(Path_Of_Folders)                  #Changing the path to the location where we want to create the new folders.
#     os.makedirs(s)                              #Finally creating the folders.



#Type2 Create folders according file-list :-
import math,os

Source_path=input("Enter The Path Of The Target Files =")
File_list_Name = [f.name for f in os.scandir(Source_path) if f.is_file()]      #Here we are getting new list of File
First_File=File_list_Name[0]
Last_file=File_list_Name[len(File_list_Name) - 1]

sp=int(First_File.split(".")[0])                               #Here we take the first-file-name(ie. starting number) from the user.
ep=int(Last_file.split(".")[0])                                #Here we take the last-file-name(ie. ending number) from the user.

frange=int(input("Enter The Range ="))               #Here we take the "file-range" for the "folder-name that we are going to create".
frange=5                                               #This is for testing purpose.
Path_Of_Folders=input("Enter Your Path Here =")       #Here we enter the path where we are going to create the folders.

my_iter=math.ceil((ep-sp+1)/frange)                    #Here we getting the "value of number of required folders".

print(f"\nThe New Folders at [{Path_Of_Folders}] are:-")

for i in range(my_iter):                       #Here we are iterating the loop according to the "number of required folders".
    n=sp+frange*i
    i=i+1
    k=n+frange-1
    # print(f"[{n}-{k}]")                       #Printing the Created-folders-name.

    s=f"{n}-{k}"                              #Storing the folders name.
    os.chdir(Path_Of_Folders)                  #Changing the path to the location where we want to create the new folders.
    os.makedirs(s)                              #Finally creating the folders.

























