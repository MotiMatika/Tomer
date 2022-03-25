import random
x=random.randint(1,100)

guess =int(input("\nךלש שוחינה : "))
print("\nבשחמה לש שוחינה ",x,"\n")
if guess>x:
    print("תחצינ\n")
else:
    print("תדספיה\n")

# print(a,b)
# c=int(input("\nwhich number is the biggest ? "))
# if c==a or c==b: 
#     if c>a or c>b:
#         print("\nןוכנ\n")
#     else:
#         print("\nןוכנ אל \n")
# else:
#     print("\nעיפומ אל\n") 