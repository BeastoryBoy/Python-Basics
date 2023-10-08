
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
m = int(input("Enter a number:"))
print("Factorial of",m,"is",fact(m))