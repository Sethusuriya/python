a=input("Enter the x:")
if a==a[ : :-1]:
    a=a
    print("True")
    print(a,"reads as",a[ : :-1],"from left to right and from right ro left.So it is a panlidrom")
else:
    print("False")
    print("From right to left it reads",a,".From left to right it reads",a[ : :-1],"Therfore it is not a palindrom")
