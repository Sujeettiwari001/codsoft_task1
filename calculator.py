num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
oper=int(input("Enter operation which you want to perform:"))
if(oper==1):
    op=num1+num2
    print(op)
elif(oper==2):
    op=num1-num2
    print(op)
elif(oper==3):
    op=num1*num2
    print(op)
elif(oper==4):
    op=num1/num2
    print(op)
else:
    print("Invalid Input")