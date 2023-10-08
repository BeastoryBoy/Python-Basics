times=int(input("ENter how many times you need to append? :"))
list1=[]
list2=[]
for i in range(0,times):
    information=input("Enter the DATA you need to append: ")
    list1.append(information)
print(list1)

times1=int(input("ENter how many times you need to append in second list? : "))
for i in range(times1):
    information1=input(("ENter the DATA you need to append: "))
    list2.append(information1)
print(list2)
list3=list1+list2
list3.sort()
print(list3)