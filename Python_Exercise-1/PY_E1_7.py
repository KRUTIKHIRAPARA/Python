#Write a program to use for loop to print the following reverse number pattern.

for a in range(5,0,-1):
    # print no
    for b in range(a,0,-1):
        print(b,end=" ")
    print()
