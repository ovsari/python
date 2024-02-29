'''sum=0
for i in range(6):
    a=int(input("enter:"))
    sum=sum+a
    print(sum)
print(sum)'''
a=[]
sum=0
print("enter 5 number")
for i in range(5):
    b=int(input("enter number "+ str(i)+":"))
    a.append(b)
print(a)
for i in a:
    sum=sum+i
print(sum)
