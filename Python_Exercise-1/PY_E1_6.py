#Write a program to count the total number of digits in a number using a while loop.For example, the number is 75869, so the output should be 5.


no = 756434
count=0

while no > 0:
    no = int(no/10)
    count += 1

print(count)
