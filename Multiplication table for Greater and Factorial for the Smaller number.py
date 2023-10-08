fac=1
a=0
b=0
x=int(input("Enter the number for x:"))
y=int(input("Enter the number for y:"))
if x>y:
    a=a+x
elif(y>x):
    a=a+y
print("The multiplication of greater number is ")
for i in range(1,11):
    print (a,"x",i,"=",a*i)
if x<y:
    b=b+x
elif y<x:
    b=b+y
while b>=1:
    fac=fac*b
    b=b-1
print("The factorial of smaller number is :",fac)