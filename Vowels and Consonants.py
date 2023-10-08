Vowels=0
Consonants=0
Str=input("Enter the String:")
for i in Str:
    if i=='a'or i=='e'or i=='i'or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        Vowels=Vowels+1
    else:
        Consonants+=1
print("Total numbers of vowels in given string is:",Vowels)
print("Total numbers of consonants in given string is:",Consonants)