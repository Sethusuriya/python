inp_string=input("enter the string to check :")
print(inp_string)
vowel=['a','e','i','o','u']
vowel_cnt=0
cons_cnt=0
for i in range(len(inp_string)):
    if inp_string[i]=='a' or inp_string[i]=='e' or inp_string[i]=='i' or inp_string[i]=='o' or inp_string[i]=='u':
        vowel_cnt+=1
    else:
        cons_cnt+=1
print("number of vowls in the given string :",vowel_cnt)
print("number of constonts in the given string :",cons_cnt)
