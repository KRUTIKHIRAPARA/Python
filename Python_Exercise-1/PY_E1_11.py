#Write a program to display all prime numbers within a range

start = int(input("Enter Start Value : "))
end = int(input("Enter End Value : "))

for no in range(start,end+1):
    for a in range(2,no):
        if no % a == 0:
            break
    else:
        print(no)
