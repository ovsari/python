salary=int(input())
age=int(input())
if (salary>=20000 or age<=25):
    loan=int(input("loan amount:"))
    if (loan<=50000):
        print("not eligible for loan")
    else:
        print("eligible for loan")
else:
    print("not eligible")
