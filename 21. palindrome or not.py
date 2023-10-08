def palindrome(a):
    for i in range(0,int(len(a)/2)):
        if(a[i]!=a[len(a)-i-1]):
            return False
        return True
string1=input("Enter the string: ")
if(palindrome(string1)):
    print("It is a palindrome")
else:
    print("it is not a palindrome")