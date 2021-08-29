# Mini project #1(Q-V71)
# Create a library class
# Display books
# Lend books - (Who owns the book if not present)
# Add book
# Return book
#
# HarryLibray = Library(ListOfBooks, Libray_name)
#
# Dictionary (Books--NameOfPerson)
#
# Create a main function and run an infinity while loop asking user for there input.




##Type1:-
# class library:
#     def __init__(self,Book_List,Name_list):
#         self.bookl=Book_List
#         self.namel=Name_list
#         self.lenddict={}
#
#
#     def display_book(self):
#         print(f"\nWe Have Following Books In Our '{self.namel}' Library:-")
#         for book in self.bookl:
#             print(f"[+]{book}")
#
#     def lend_book(self,user,bookn):
#         if bookn not in self.lenddict.keys():
#             self.lenddict.update({bookn:user})
#             print(f"\nLender-Book Database Has Been Updated.Now You Can Take The Book...!!")
#
#         else:
#             print(f"Book Is Already Being Used By {self.lenddict[bookn]}")
#
#     def add_book(self,booka):
#         self.bookl.append(booka)
#         print(f"\nA Book Has Been Added To The Library!!")
#
#     def return_book(self,bookr):
#         self.lenddict.pop(bookr)
#         print("Thank You!!")
#
# if __name__ == '__main__':
#     harry=library(["Pentesting","Ethical hacking","Kali Linux","Termux Basics","C++ For The Beginners","Python","Linux","Web Development","HTML","CSS","JavaScript"],"Lucifer-World")
#
#     while(True):
#         user_choice=int(input(f"\nWelcome To The '{harry.namel}' library.Select Your Choice To Continue:- \n1.)Display Books \n2.)Lend A Book \n3.)Add A Book \n4.)Return A Book \nEnter Your Choice here ="))
#
#         if user_choice==1:
#             harry.display_book()
#
#         elif user_choice==2:
#             user=input(f"\nEnter Your Name =")
#             bookn=input("Enter The Book That You Want To Lend =")
#             harry.lend_book(user,bookn)
#
#         elif user_choice==3:
#             booka=input(f"\nEnter The Name Of The Book You Want To Add =")
#             harry.add_book(booka)
#
#         elif user_choice==4:
#             bookr=input(f"\nEnter The Name Of The Book You Want To Return =")
#             harry.return_book(bookr)
#
#         else:
#             print("Not A Valid Option!!")
#
#         user_choice2=""
#         while(user_choice2!="q" and user_choice2!="c"):
#             user_choice2=input(f"\nPress 'q' To Quit And 'c' To Continue = ")
#             if user_choice2=="q":
#                 exit()
#
#             elif user_choice2=="c":
#                 continue




# #Type2:-
# class new_expt:
#     def __init__(self,clst1,):
#         self.dictt={}
#         self.clst=clst1
#
#     def display_colour(self,a2):
#         print(f"\nWe Have Following Colours:-")
#         for cl in self.clst:
#             # self.mls.update(a2)
#             # print(cl,a1,a2)
#             # print(f"[+]{cl} {len(self.clst)}")
#             if cl==a2:
#                 self.clst.remove(a2)
#             # else:
#             #     continue
#
#         # print(*self.clst,sep='\n')
#         print(*self.clst,sep='\n')
#
#     def testdict(self,a1,a2):                                         #lend_book Part
#         if a1 in self.dictt.keys() or a2 in self.dictt.values():
#             print("This is a duplicate information!!")
#             print(self.dictt)
#
#         else:
#             # j1=open("dictlog.txt","r+")
#             j1=open("dictlog.txt","a")
#             self.dictt.update({a1:a2})
#             j1.write(f"[{a1}:{a2}]\n")
#             # j1.write(f"{self.dictt} \n")
#             j1.close()
#
#
#
# teady=new_expt(["red","blue","yellow","black","green","white"])
#
#
# while(True):
#     a1=int(input("Enter Your No ="))                    #This is the "key" of the dictionery
#     a2=input("Enter Your colour =")                   #This is the "value" of the dictionery
#     teady.display_colour(a2)
#     teady.testdict(a1,a2)
#
#     user_choice2=""
#     while(user_choice2!="q" and user_choice2!="c"):
#         user_choice2=input(f"\nPress 'q' To Quit And 'c' To Continue = ")
#         if user_choice2=="q":
#             exit()
#
#         elif user_choice2=="c":
#             continue



#Type3:-
class library:
    def __init__(self,Book_List,Name_list):
        self.bookl=Book_List
        self.namel=Name_list
        self.lenddict={}


    def display_book(self):
        print(f"\nWe Have Following Books In Our '{self.namel}' Library:-")

        j1=open("dictlog.txt","a")
        j1.write(f"\n\n[Book_list] of '{self.namel}':-")
        for book in self.bookl:
            # j1=open("dictlog.txt","a")
            j1.write(f"\n{book}")

            if book in self.lenddict.keys():
                self.bookl.remove(book.casefold())
                # print(f"[+]{book}")


        print(*self.bookl,sep='\n')
        j1.close()
    def lend_book(self,bookn,user):
        if bookn not in self.lenddict.keys():
            j1=open("dictlog.txt","a")
            # j1.write(f"\nIssued Book-User_Name Log:-")

            self.lenddict.update({bookn.casefold():user})
            print(f"\nLender-Book Database Has Been Updated.Now You Can Take The Book...!!")

            j1.write(f"\n\nIssued Book-User_Name Log:-\n[Issued] [{bookn}] is issued by [{user}]")
            j1.close()

        else:
            print(f"Book Is Already Being Used By {self.lenddict[bookn]}")

    def add_book(self,booka,usera):
        j1=open("dictlog.txt","a")
        # j1.write(f"Add_Book Book-User_Name Log:-")

        self.bookl.append(booka.casefold())
        print(f"\nA Book Has Been Added To The Library!!")

        j1.write(f"\n\nAdd_Book Book-User_Name Log:-\n[Add_Book] [{booka}] is added by [{usera}]")
        j1.close()

    def return_book(self,bookr,userr):
        j1=open("dictlog.txt","a")
        # j1.write(f"Returned Book-User_Name Log:-")

        self.lenddict.pop(bookr.casefold())
        print("Thank You!!")

        j1.write(f"\n\nReturned Book-User_Name Log:-\n[Return_Book] [{bookn}] is returned by [{userr}]")
        j1.close()

if __name__ == '__main__':
    harry=library(["Pentesting","Ethical hacking","Kali Linux","Termux Basics","C++ For The Beginners","Python","Linux","Web Development","HTML","CSS","JavaScript"],"Lucifer-World")

    while(True):
        user_choice=int(input(f"\nWelcome To The '{harry.namel}' library.Select Your Choice To Continue:- \n1.)Display Books \n2.)Lend A Book \n3.)Add A Book \n4.)Return A Book \nEnter Your Choice here ="))

        if user_choice==1:
            harry.display_book()

        elif user_choice==2:
            user=input(f"\nEnter Your Name =")
            bookn=input("Enter The Book That You Want To Lend =")
            harry.lend_book(bookn,user)

        elif user_choice==3:
            usera=input(f"\nEnter Your Name =")
            booka=input(f"Enter The Name Of The Book You Want To Add =")
            harry.add_book(booka,usera)

        elif user_choice==4:
            userr=input(f"\nEnter Your Name =")
            bookr=input(f"Enter The Name Of The Book You Want To Return =")
            harry.return_book(bookr,userr)

        else:
            print("Not A Valid Option!!")

        user_choice2=""
        while(user_choice2!="q" and user_choice2!="c"):
            user_choice2=input(f"\nPress 'q' To Quit And 'c' To Continue = ")
            if user_choice2=="q":
                exit()

            elif user_choice2=="c":
                continue
