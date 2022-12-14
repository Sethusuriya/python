madurai=int(input("enter the distance: "))
chennai=int(input("enter the distance: "))
goa=int(input("enter the distance: "))
if(madurai>chennai)and(madurai>goa):
    print("madurai is longest")
elif(chennai>madurai)and(chennai>goa):
    print("chennai is longest")
else:
    print("goa is longest")
