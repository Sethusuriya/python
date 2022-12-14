n=int(input("how many count"))
n1,n2=0,1
count=0
if n<=0:
    print("please enter a positive integer")
elif n==1:
    print("fibronacci series upto",n,":")
    print(n1)
else:
    print("fibronacci series:")
    while count<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
     #   print(count,n)
