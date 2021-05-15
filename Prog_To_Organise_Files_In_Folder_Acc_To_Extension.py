#Program to create multiple folders  and  organise files in folder according to their extension  at same path:



#Type1 Creating Folders:-
#import os,shutil,time
# os.mkdir("n")
# os.makedirs("no/4/5/gh/kj")              #Creating Folder inside Folder.
# os.makedirs("no")



#Type2 Program to create multiple folders  and  organise files in folder according to their extension  at same path:-

# import os,shutil,time
#
# # Folder_CP=input("Enter Your Path To Organise Files In Folder According =")        #Here we provide the path for creating the folders.
#
# print(f"\nCreating Folders..")
# time.sleep(2)
# folders=["My_Videos","My_Music","My_Documents","My_Programs","My_Compressed_Files","My_Pictures","My_Other-Files"]   #Here we give the name of the folders.
# for folder in folders:
#     os.mkdir(os.path.join(Folder_CP,str(folder)))                                                        #Here we are creating the folders.
#
# File_list_name = [f.name for f in os.scandir(Folder_CP) if f.is_file()]      #Here we are getting list of File.
# # print(*File_list_name, sep="\n")
#
# Video_Extensions=["mp4","mkv","webm"]                                             #Video_Extensions
# Music_Extensions=["mp3","m4a"]                                                   #Music_Extensions
# Document_Extensions=["txt","pdf","doc","docx","xls","xlsx","ppt","pptx","rtf"]  #Document_Extensions
# Program_Extensions=["exe"]                                                      #Program_Extensions
# CompressedFile_Extensions=["rar","zip","7z"]                                     #CompressedFile_Extensions
# Picture_Extensions=["png","jpg","jpeg"]                                           #Picture_Extensions
#
#
# print(f"\nMoving Files To Their Respective Folders..")
# time.sleep(2)
# for item in File_list_name:
#     l=item.split('.')[1]
#
#     for jk in range(len(Video_Extensions)):
#         if Video_Extensions[jk]==l:
#             # print(f"\nThe Video items are = {item}")
#             shutil.move(f"{Folder_CP}/{item}",f"{Folder_CP}/My_Videos")    #Moving The Video Files To "My_Videos" Folder.
#
#     for jk1 in range(len(Music_Extensions)):
#         if Music_Extensions[jk1]==l:
#             # print(f"\nThe Music items are = {item}")
#             shutil.move(f"{Folder_CP}/{item}",f"{Folder_CP}/My_Music")     #Moving The Audio Files To "My_Music" Folder.
#
#     for jk2 in range(len(Document_Extensions)):
#         if Document_Extensions[jk2]==l:
#             # print(f"\nThe Document items are = {item}")
#             shutil.move(f"{Folder_CP}/{item}",f"{Folder_CP}/My_Documents")  #Moving The Document Files To "My_Documents" Folder.
#
#     for jk3 in range(len(Program_Extensions)):
#         if Program_Extensions[jk3]==l:
#             # print(f"\nThe Program items are = {item}")
#             shutil.move(f"{Folder_CP}/{item}",f"{Folder_CP}/My_Programs")   #Moving The Program Files To "My_Programs" Folder.
#
#     for jk4 in range(len(CompressedFile_Extensions)):
#         if CompressedFile_Extensions[jk4]==l:
#             # print(f"\nThe Compressed items are = {item}")
#             shutil.move(f"{Folder_CP}/{item}",f"{Folder_CP}/My_Compressed_Files")   #Moving The Compressed_Files To "My_Compressed_Files" Folder.
#
#     for jk5 in range(len(Picture_Extensions)):
#         if Picture_Extensions[jk5]==l:
#             # print(f"\nThe Picture items are = {item}")
#             shutil.move(f"{Folder_CP}/{item}",f"{Folder_CP}/My_Pictures")   #Moving The Picture Files To "My_Pictures" Folder.
#
#
# New_list_name = [f.name for f in os.scandir(Folder_CP) if f.is_file()]      #Here we are getting new list of File.
# for item in New_list_name:
#     for jk6 in range(len(New_list_name)):
#         shutil.move(f"{Folder_CP}/{item}",f"{Folder_CP}/My_Other-Files")    #Moving The Other-Left-Over Files To "My_Other-Files" Folder.
#
# print(f"\nCongratulations!! Your Files Have Been Organised In Folders According To Their Extension..!!")



#Type3(Updated version of Type2):-
import os,shutil

#Taking the source path and scanning the files present in it.
Source_path= input("Enter the path where your target files are present: ")
File_list_Name = [f.name for f in os.scandir(Source_path) if f.is_file()]

#Creating the folders according to extensions.
folders=["My_Videos","My_Music","My_Documents","My_Programs","My_Compressed_Files","My_Pictures","My_Other-Files"]   #Here we give the name of the folders.
for folder in folders:
    os.mkdir(os.path.join(Source_path,str(folder)))         #Here we are creating the folders.

#Creating Tuple of extensions.
Video_Extensions=("mp4","mkv","webm")
Music_Extensions=("mp3","m4a")
Document_Extensions=("txt","pdf","doc","docx","xls","xlsx","ppt","pptx","rtf")
Program_Extensions=("exe")
CompressedFile_Extensions=("rar","zip","7z")
Picture_Extensions=("png","jpg","jpeg")

#Checking and moving the files acc. to its extension.
for i in range(len(File_list_Name)):
    if File_list_Name[i].endswith(Video_Extensions):
        shutil.move(f"{Source_path}/{File_list_Name[i]}",f"{Source_path}/My_Videos")

    elif File_list_Name[i].endswith(Music_Extensions):
        shutil.move(f"{Source_path}/{File_list_Name[i]}",f"{Source_path}/My_Music")

    elif File_list_Name[i].endswith(Document_Extensions):
        shutil.move(f"{Source_path}/{File_list_Name[i]}",f"{Source_path}/My_Documents")

    elif File_list_Name[i].endswith(Program_Extensions):
        shutil.move(f"{Source_path}/{File_list_Name[i]}",f"{Source_path}/My_Programs")

    elif File_list_Name[i].endswith(CompressedFile_Extensions):
        shutil.move(f"{Source_path}/{File_list_Name[i]}",f"{Source_path}/My_Compressed_Files")

    elif File_list_Name[i].endswith(Picture_Extensions):
        shutil.move(f"{Source_path}/{File_list_Name[i]}",f"{Source_path}/My_Pictures")

    else:
        shutil.move(f"{Source_path}/{File_list_Name[i]}",f"{Source_path}/My_Other-Files")

print(f"\nCongratulations!! Your Files Have Been Organized In Folders According To Their Extension..!!")




















