def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("Select the operator\n"\
      "a.Addition"\
      "b.Subtraction"\
      "c.Multiplication"\
      "d.Division"\
          )
selection=input("Enter the Option:")
n=int(input("Enter First Number:"))
x=int(input("Enter Second Number:"))
for i in selection:
      if i=='a':
          print(n,"+",x,"=",add(n,x))
      elif i=='b':
          print(n,"-",x,"=",sub(n,x))
      elif i=='c':
          print(n,"*",x,"=",mul(n,x))
      elif i=='d':
          print(n,"/",x,"=",div(n,x))
      else:
          print("Invalid syntax")
         