b=int(input("enter the number :"))
for i in range(2,b*2):
    k=0.0
    for j in range (2,i):
        k=k+0.1
        print('%.1f'%k,end=" ")
    print()
  
