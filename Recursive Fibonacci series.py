b = int(input("Enter the n term: "))
def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
if b<=0:
    print("Enter the positive integer")
else:
    for i in range(b):
        print(fib(i))
    