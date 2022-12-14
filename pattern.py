print("1.*")
print("2.**")
print("3.1,1")
print("4.1,2")
b=int(input("enter the b number"))
n=int(input("enter the number of rows"))
if(b==1):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif(b==2):
    for i in range(n-1,1,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif(b==3):
    for i in range(1,n):
        for j in range(0,i):
            print(i,end=" ")
        print()
elif(b==4):
    for i in range(1,n+1):
        for j in range(1,i):
            print(j,end=" ")
        print()

  
