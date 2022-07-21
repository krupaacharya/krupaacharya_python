# age=float(input("enter your age"))
# if age>=18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")

    
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# if a>b:
#     print("a is greater to all")
# elif a>c:
#     print("a is greater to all")
# # elif b>c:
# #     print("b is greaterthan c")
# else:
#     print("b is smaller")

#nested if statement
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b:
    if a>c:
        print("a is greater to all")
    else:
        print("c is greater to all")
else:
    if b>c:
        print("b is greater")
    else:
        print("c is greater")
