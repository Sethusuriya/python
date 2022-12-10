p=int(input("enter the previous reading"))
c=int(input("enter the current reading value"))
u=c-p
print("unit_consumed=",u)
if (u<=100):
    print("your bill amount is",u*3.46,"rs")
elif(u>=101<500):
    print("your bill amount is",u*7.43,"rs")
elif(u>=501):
    print("your bill ampunt is",u*10.32,"rs")
