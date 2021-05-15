# Program to rename multiple files to its initial part of the name at once:
# Eg.  Let Initial_file_name="The Avengers @ 720p (2018).mp4" and Required_file_name="The Avengers.mp4"
#      Then 'spt1=@' and fextension=".mp4"  Done!!


import os
New_dir=os.chdir(input("Enter your path of file here: "))                     #Here we are taking the 'path from the user' where we have to rename the files.
print("\nThis is the new 'current working dir' =",[ os.getcwd() ])      #Here we print the 'new given path'..

spt1=input("Enter the 'char' or 'string' just after the required name: ")
fextension=input("Enter the file extension here with a '.' =")
File_list=os.listdir(New_dir)           #Here we are getting list of File-Folder

# print(File_list)

for i in range(len(File_list)):         #Here we are iterating the loop for number of time 'the no. of elements in list'.
    Split1 = File_list[i].split(spt1)[0]   #Here we split each string of the list(ie, 'File_list') by "_-_"
    
    d=f"{Split1}{fextension}"
    # print(d)
    os.rename(File_list[i],d)          #Here we rename the file as "os.rename(initial_name,final_name)"

print("Congratulations!! The file-names are changed!!")