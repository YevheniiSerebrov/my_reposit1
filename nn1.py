a=float(input("Input 1-st number "))
d=input("Input + - * or / ")
c=float(input("Input 2-nd number "))
if d == "+":
    print("result is ", a+c)
elif d=="-":
    print("result is ", a-c)
elif d== "*":
    print("Result is ", a*c)
try:
    if d == "/":
        print("result is ", a/c)
except:
    print("res = infinity")

