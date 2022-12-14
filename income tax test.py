#calculate income tax
income=int(input("enter your income: "))
if(income<=150000):
    print("no tax enjoy")
elif(income>=150001)and(income<=300000):
    print("tax 10% :",10/100*income)
elif(income>=300001)and(income<=500000):
    print("tax 20% :",20/100*income)
elif(income>=500001):
    print("tax 30% :",30/100*income)
