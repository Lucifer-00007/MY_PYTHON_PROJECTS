#Q- Take a variable and typecast it to boolean. Make a condition to check weather it(ie bool) is true or false. Now if the condition is True print a rightangle triangle else inverted right angle triangle for  vice versa.

#Type1, Without typecasting to boolean:-
# Enter_the_length= int(input("Enter the length= "))
# no_to_check_if= int(input("Number to check if= "))
#
# if (Enter_the_length==no_to_check_if):
#
#     for j in range(Enter_the_length):
#         for i in range(j+1):
#             print("*", end="")
#         print()                    #here "print()" prints nothing. "print()" is used to take the program to the next line.
#
#
#
# else:
#     for j in range(Enter_the_length):
#         for k in range(Enter_the_length - j):
#             print("*", end="")
#         print()



#Type2,  By typecasting to boolean:-
Enter_the_length= int(input("Enter the length= "))
Typecast_str_int_bool_to_check_if= bool(int(input("Enter 0 or 1= ")))      #here we have typecasted str value to Integer. Then Integer to Boolean.
print("the condition is= ",Typecast_str_int_bool_to_check_if)              #to check the bool value

if Typecast_str_int_bool_to_check_if== True:               #Condition for right angle triangle
    for j in range(Enter_the_length):
        for i in range(j+1):
            print("*", end="")
        print()                    #here "print()" prints nothing. "print()" is used to take the program to the next line.

elif Typecast_str_int_bool_to_check_if== False:            #Condition for inverted right angle triangle
    for j in range(Enter_the_length):
        for k in range(Enter_the_length - j):
            print("*", end="")
        print()


