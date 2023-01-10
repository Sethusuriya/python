a=int(input("Enter the value = "))
b=int(input("Enter the value = "))
print("CHOICE A. [addition]")
print("CHOICE B. [subraction]")
print("CHOICE C. [multiple]")
print("CHOICE D. [division]")
n=input("Enter the CHOICE : ")
if(n=='A'):
      add=a+b
      print("Addition VALUE:",a,"+",b,"=",add)
elif(n=='B'):
    sub=a-b
    print("Subraction Value: ",a,"-",b,"=",sub)
elif(n=='B'):
    mult=a*b
    print("Multiple Value: ",a,"*",b,"=",mult)
elif(n=='D'):
    divi=a/b
    print("Division Value: ",a,"/",b,"=",divi)
