L=[3,5,1,23,12,87,445,35,67,22,13]
divisible_by_5=[]
divisible_by_7=[]
divisible_by_both_5and7=[]
for i in range (len(L)):
    if(L[i]%5==0):
        divisible_by_5.append(L[i])
    if(L[i]%7==0):
        divisible_by_7.append(L[i])
    if(L[i]%5==0) and (L[i]%7==0):
        divisible_by_both_5and7.append(L[i])
print("the number divisible by 5 =",sorted(divisible_by_5))
print("the number divisible by 7 =",sorted(divisible_by_7))
print("the number divisible by both 5 and 7 =",sorted(divisible_by_both_5and7))
