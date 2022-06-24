#Write a program to print the following start pattern using the for loop.

n = int (input ("enter number : "))

for a in range(1,n):
    for j in range(1,a+1):
        print("*",end=" ")
    print()

for a in range(1,n-1):
    for j in range(n-1,a,-1):
        print("*",end=" ")
    print()
