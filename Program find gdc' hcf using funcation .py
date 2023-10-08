n = int (input("Enter First number: "))
m = int(input("Enter second number: "))
def gcd(a,b):
    if a<b:
        smaller=a
    else:
        smaller:b
    for i in range(1,smaller+1):
        if a%i==0 and b%i==0:
            sob=i
    return sob
print(gcd(n,m))

    