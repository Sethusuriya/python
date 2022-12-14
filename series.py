#pgm to find the sum of n numbers

n=int(input("enter the number N:"))
sum=0
evensum=0
evenlist=[]
oddsum=0
oddlist=[]
for i in range(1,n+1):
    if i%2==0:
        evensum=evensum+i
        evenlist.append(i)
    else:
        oddsum=oddsum+i
        oddlist.append(i)
    sum=sum+i
  #  print(i)
print("sum of ",n," numbers is :",sum)
print("Sum of odd numbers is :",oddsum)
print("sum of even numbers is :",evensum)
print("odd numbers in the given series are :", oddlist)
print("even numbers in the given series are :", evenlist)

  
            
