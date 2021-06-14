#Exercise 5- Health management system :-
#Q- 3 clients, 6 files. Ask weather to retrive or add data to the file.



print("Select a number:","\n 1.Lock","\n 2.Retrive")
a =int(input("Enter= "))
# print(a)

def getmytime():
    import datetime
    return datetime.datetime.now()
# a=getmytime()
# print(f"[ {a} ]")

#------To add new items----------#
if a==1: 
    print("Select a number:", "\n 1.Alok", "\n 2.Anuj","\n 3.Shivam")
    b= int(input("Enter= "))
    # print(b)

    if b==1:       #-----------------------------Alok------------------------------#
        print("Select a number:", "\n 1.Dite", "\n 2.Exercise")
        d = int(input("Enter= "))
        if d==1:  #dite
            j=open("Alok_Dite.txt","a")
            j1=input("add your food= ")
            p = getmytime()
            j.write(f"[ {p} ],{j1} \n")
            j.close()
        else:     #exercise
            j1 = open("Alok_exercise.txt", "a")
            j3=input("add new exercise= ")
            p1=getmytime()
            j1.write(f"[ {p1} ],{j3} \n")
            j1.close()

    elif b==2:     #-----------------------------Anuj------------------------------#
        print("Select a number:", "\n 1.Dite", "\n 2.Exercise")
        d = int(input("Enter= "))
        if d == 1:  #dite
            k=open("Anuj_dite.txt","a")
            k2=input("add your food= ")
            q=getmytime()
            k.write(f"[ {q} ],{k2} \n")
            k.close()
        else:      #exercise
            k1= open("Anuj_exercise.txt", "a")
            k3=input("add new exercise= ")
            q1=getmytime()
            k1.write(f"[ {q1} ],{k3} \n")
            k1.close()

    else:          #-----------------------------Shivam-----------------------------#
        print("Select a number:", "\n 1.Dite", "\n 2.Exercise")
        d = int(input("Enter= "))
        if d == 1:  #dite
            m=open("Shivam_dite.txt","a")
            m2=input("add your food= ")
            r=getmytime()
            m.write(f"[ {r} ],{m2} \n")
            m.close()
        else:       #exercise
            m1 = open("Shivam_dite.txt", "a")
            m3=input("add new exercise= ")
            r1= getmytime()
            m1.write(f"[ {r1} ],{m3} \n")
            m1.close()

            
            
#------To view the content----------#
else:    
    print("Select a number:", "\n 4.Alok", "\n 5.Anuj", "\n 6.Shivam")
    c = int(input("Enter= "))
    # print(c)
    if c==4:      #-----------------------------Alok------------------------------#
        print("Select a number:", "\n 1.Dite", "\n 2.Exercise")
        d = int(input("Enter= "))
        if d == 1:  # dite
            j = open("Alok_dite.txt")
            print(j.read())
            j.close()
        else:  # exercise
            j1 = open("Alok_exercise.txt")
            print(j1.read())
            j1.close()

    elif c==5:    #-----------------------------Anuj------------------------------#
        print("Select a number:", "\n 1.Dite", "\n 2.Exercise")
        d = int(input("Enter= "))
        if d == 1:  # dite
            k = open("Anuj_dite.txt")
            print(k.read())
            k.close()
        else:  # exercise
            k1 = open("Anuj_exercise.txt")
            print(k1.read())
            k1.close()

    else:         #-----------------------------Shivam-----------------------------#
        print("Select a number:", "\n 1.Dite", "\n 2.Exercise")
        d = int(input("Enter= "))
        if d == 1:  # dite
            m = open("Shivam_dite.txt")
            print(m.read())
            m.close()
        else:  # exercise
            m1 = open("Shivam_exercise.txt")
            print(m1.read())
            m1.close()






