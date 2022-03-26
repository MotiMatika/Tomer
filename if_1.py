import random
x=random.randint(1,100)

# guess =int(input("\nךלש שוחינה : "))
# print("\nבשחמה לש שוחינה ",x,"\n")
# if guess>x:
#     print("תחצינ\n")
# else:
#     print("תדספיה\n")




#מהו המספר הגדול ביותר מבין שניים
# import random
# a=random.randint(1,100)
# b=random.randint(1,100)
# print(a,b)
# qu=int(input("\n? רתויב לודגה רפסמה "))

# if qu>a or qu>b:
#    print("\nדאמ הפי\n")
# else:
#     print("\nןוכנ אל \n")



#מהו המספר הגדול ביותר מבין שלשה
import random
a=random.randint(1,100)
b=random.randint(1,100)
c=random.randint(1,100)
print(a,b,c)
qu=int(input("\n? רתויב לודגה רפסמה "))

if a>b and a>c and qu==a:
    print("\nדאמ ןוכנ")
elif a>b and a<c and qu==c:
    print("\nדאמ ןוכנ")
elif a<b and b>c and qu==b:
    print("\nדאמ ןוכנ")
elif a<b and b<c and qu==c:
    print("\nדאמ ןוכנ")
elif qu!=a and qu!=b and qu!=c:
    print("\nבוט האור אל התא")
else:
    print("\nהעוט התא")







 