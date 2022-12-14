number_list=[]
n=int(input("enter the list size"))
print("/n")
for i in range(0,n):
    print("enter number at inex",i, )
    item=int(input())
    number_list.append(item)
print("user list is",number_list)
p=sorted(number_list)
print("the greatest number from the list:",p[-item])
 
