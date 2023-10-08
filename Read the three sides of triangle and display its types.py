a=int(input("Enter the value: "))
b=int(input("Enter the value: "))
c=int(input("Enter the value: "))
if (a==b==c):
    print("It's the Equilateral Triangle.")
elif (a==b or b==c or c==b):
    print("It's the Isosceles Triangle.")
else:
    print("It's the Scalene Triangle.")
