# Program to read the content of json file.


import json    
# import re            #Here we have used 'Regular_Expression module to filter out a part of string.


fp1=input("Enter the JSON file path here: ")

# tag_in_json=input("Enter the KEY here: ")

# f = open(fp1,)
f = open(fp1 , encoding="UTF-8")   #Here we have loaded the file at 'fp1 location'
# f = open(fp1,errors="ignore")

data = json.load(f)   #Here we are filtering out the json data in python format.


for i in data:
	print(i,end="\n\n\n \n\n\n")
	# print(i[tag_in_json],end="\n\n\n \n\n\n")

f.close()


