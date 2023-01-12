a=int(input("enter the number: "))
b=["a","e","i","o","u"]
s=[]
for i in b:
    for j in b:
            if(a==1) & (i==j):
                s.append(i)
            elif(a==2) & (i<=j):
                s.append(i+j)
            else:
                continue
print(s)
