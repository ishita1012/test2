def fib(N):
    a,b=0,1
    for i in range(N):
        print(a, end=' ')
        a,b=b,a+b
        

n= int(input("enter N: "))
print("fibonnaci is as follows: ")
fib(n)
