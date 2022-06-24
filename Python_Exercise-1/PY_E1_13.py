#Write a program to use the loop to find the factorial of a given number.

no = int(input("Enter Number : "))

f = 1

for i in range(no,0,-1):
    f *= i
else:
    print("Factorial of",no,"is : ",f)
