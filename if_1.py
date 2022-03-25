import random
x=random.randint(1,100)

guess =int(input("\nךלש שוחינה : "))
print("\nבשחמה לש שוחינה ",x,"\n")
if guess>x:
    print("תחצינ\n")
else:
    print("תדספיה\n")