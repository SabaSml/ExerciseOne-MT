
from cmath import sin
import math
class color:
   BOLD = '\033[1m'
   END = '\033[0m'

while True:
    print(color.BOLD +"Welcome, pls type ur operation"+ color.END)
    print(color.BOLD +"log  sin  tan   sqrt   +   -   *   /   **   "+ color.END)

    operator=input()
    if operator=="exit":
        break
    elif operator=="sin" or operator=="log" or operator=="fact" or operator=="tan" or operator=="sqrt":
        a=float(input())
    else:
        a = float(input())
        b = float(input())

    if operator=="+":
        result = a+b

    elif operator == "-":
        result= a-b

    elif operator == "*":
        result=a*b

    elif operator=="**" or operator=="^":
        result= math.pow(a,b)

    elif operator=="sin":
        result=math.sin(a)

    elif operator=="log":
        result=math.log(a)

    elif operator=="fact":
        result=math.factorial(a)
    
    elif operator=="tan":
        result=math.tan(a)

    elif operator=="sqrt":
        result=math.sqrt(a)

    elif operator=="/":
        if b==0:
            print("cannot devide by zero")
        else:
            result=a/b



    print(result)