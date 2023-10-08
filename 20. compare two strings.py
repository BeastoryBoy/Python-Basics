firstString=input("ENter the first string: ")
secondString=input("ENter the second string: ")

def compare(a,b):
    if(len(a)==len(b)):
        for i in range(0,len(a)):
            for j in range(0,len(b)):
                if(a[i]!=b[j]):
                    return False
                    break
                return True
            
if(compare(firstString,secondString)):
    print("They both are same")
else:
    print("They both are not same")