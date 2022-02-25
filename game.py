import random

x=random.randint(0,100)
count = 0
while True:
    user_number =int(input())
    if user_number==x:
        count += 1
        print("well done")
        print("Congratulations you did it in ",
              count, " try")
        break

    elif user_number>x:
        count += 1
        print("boro paiin")

    elif user_number<x:
        count += 1
        print("boro bala")