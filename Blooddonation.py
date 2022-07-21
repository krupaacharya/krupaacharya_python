from turtle import window_height

name = (input("enter the name:\n"))
age = int(input("enter the age:\n"))
weight= int(input("enter your weight:\n"))
height = float(input("enter your height:\n"))
bloodgroup =(input("enter your bloodgroup:\n "))
if age<18 or weight>45 or height<5.4 :
        print("you are eligible for blood donate")
else:
        print("you are not eligible for blood donate")

