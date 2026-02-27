# area of traiangle
import math

num1=float(input("Enter your first number: "))
num2=float(input("Enter your last number: "))
num3=float(input("Enter your third number: "))
s= (num1+num2+num3)/2
print("The product is: ", s)
area=math.sqrt(s*(s-num1)*(s-num2)*(s-num3))
print("The area is: ", area)