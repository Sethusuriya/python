list1=[2,101,6,8,7,45,232,41]
print("before sorting",list1)
a=sorted(list1)
print ("after sorting",a)
b=int(input("enter the bth maximum position"))
c=int(input("enter the cth minimum position"))

print("bth maximum elentment is :", a[-b])
print("cth minimum elentment is :", a[c-1])
