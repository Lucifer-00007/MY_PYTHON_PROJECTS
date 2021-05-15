#In this program we will rename all Files in a directory by "shuffling the strings of the initial file_name" according to the user's choice to get the final_name:
# Eg.  If Initial_name= "AnimePahe1_Detective_Conan_-_460_396p_DCTP.mp4 - Copy (2) - Copy.txt"  ,
#      Split1= "_-_"  ,  Split2= "_396p" and In_Between_String=")" ,
#  	   then  Final_name="460) AnimePahe1_Detective_Conan_-__396p_DCTP.mp4 - Copy (2) - Copy.txt"   
 


import os
New_dir=os.chdir(input("Enter your path here ="))   #Here we are taking the 'path from the user' where we have to rename the files.
print("\nThis is the new 'current working dir' =",[ os.getcwd() ])      #Here we print the 'new given path'..


# spt1="_-_"    			#This value is taken for testing purpose.
spt1=input("Enter the 'char' or 'string' just before the shuffling string :")    			
# spt2="_396p"            #This value is taken for testing purpose.
spt2=input("Enter the 'char' or 'string' just after the shuffling string :")    			
# In_Between_String=")"   #This value is taken for testing purpose.
In_Between_String=input("Enter the string you want to add between shuffling-string and the rest name('you can also leave it empty') : ")   


File_list_Path = [f.path for f in os.scandir(New_dir) if f.is_file()]

File_list=[f.name for f in os.scandir(New_dir) if f.is_file()]           #Here we are getting list of Files
print("\nThis was the initial name-list of files:")
print(*File_list, sep="\n")
print(f"\n\n")

for i in range(len(File_list)):         #Here we are iterating the loop for number of time 'the no. of elements in list'.
    Split1 = File_list[i].split(spt1)  #Here we split each string of the list(ie, 'File_list') by "_-_"
    Split2 = Split1[1].split(spt2)    #Here we split each string of 'Split1[1]'(ie, second-part[1] of  the strings of Split1) by "_" and store the first part of the string(ie. [0] in Split2)
    # d=f"{Split2[0]}{In_Between_String} {Split1[0]}{spt1}{spt2}{Split2[1]}"
    # d=f"({Split2[0]}{In_Between_String} {Split1[0]}{Split2[1]}"
    d=f"({Split2[0]} {In_Between_String} {Split1[0]}{Split2[1]}"
    
    # print(File_list_Path[i])      #This value is taken for testing purpose. 
    # print(d)                     #This value is taken for testing purpose. 
    os.rename(File_list[i],d)     #Here we rename the file as "os.rename(initial_name,final_name)"

New_File_list = [f.name for f in os.scandir(New_dir) if f.is_file()]      #Here we are getting new list of File
print("This is the final name-list of files:")
print(*New_File_list, sep="\n")
print(f"\n\n")


print("Congratulations!! The file-names are changed!!")

