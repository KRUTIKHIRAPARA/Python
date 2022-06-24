#Display Fibonacci series up to 10 terms

a= 0
an = 1

for i in range(1,11):
    print(a,end=" ")
    tmp = a + an
    a = an
    an = tmp
