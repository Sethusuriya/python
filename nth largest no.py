# list of numbers
list1 = [10, 44, 60, 45, 101]
print("before sorting :",list1)
print("after sorting :",sorted(list1))
# printing the maximum element
print("Largest element is:", max(list1))
n=int(input("enter the position"))
a=sorted(list1)

print("nth largest is :",a[-n])
