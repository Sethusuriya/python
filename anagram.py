string1=list(input("enter the string1: "))
string2=list(input("enter the string2: "))
string1.sort()
string2.sort()
if string1==string2:
    print('string are anagram')
else:
    print('string are not anagram')
