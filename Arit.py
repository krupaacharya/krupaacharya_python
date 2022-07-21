import sympy
from sympy import isprime
n= int(input('Enter number:'))
x = sympy.isprime(n)
if x==True:
    print("prime number")
else :
    print("not a prime number")