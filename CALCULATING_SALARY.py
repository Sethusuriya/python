#program to calculate the salary of an employee
basicpay=int(input("enter the basic pay"))
HRA=10/100*basicpay
TA=5/100*basicpay
salary=basicpay+HRA+TA
print("basic pay =",basicpay)
print("home rent allowance=",HRA)
print("travelling allowancr=",TA) 
print("overall salary=",salary)
