sent1=input("enter the sentence 1: ")
sent2=input("enter the sentence 2: ")
a=sent1.split()
b=sent2.split()
a=set(a)
b=set(b)
print(a.symmetric_difference(b))

