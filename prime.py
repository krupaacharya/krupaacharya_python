from ast import Num


num=int(input("Enter a number"))
l =(2,3,5,7,11,13,17,19,23,29,31,37,41,43,
    47,53,59,61,67,71,73,79,83,89,97)
if num>1:
    if num in(l):
        print(num,"it is a prime number")
    else:
        print(num,"it is not a prime number")
else:
    print("number is prime")
    # for i in range(2,n):
    #     if n%i==0:
    #         print("not a prime")
    #         break
    # else:
    #         print("Number is prime")