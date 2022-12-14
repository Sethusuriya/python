#program to print the pattern
b=int(input("enter the number :"))
for i in range(1,b+1):
    for j in range(i):
        print(2**i,end=" ")
    print()
