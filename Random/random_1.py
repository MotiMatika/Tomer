    # @@@          פעילות מספר 1        @@@
#                        ?מי ינחש מספר גדול מחברו   
# התמודדות מול מספר אקראי של המחשב מול המספר של השחקן

# import random
# x=random.randint(1,100)

# guess =int(input("\nךלש שוחינה : "))
# print("\nבשחמה לש שוחינה ",x,"\n")
# if guess>x:
#     print("תחצינ\n")
# else:
#     print("תדספיה\n")




#                   @@@          פעילות מספר 2        @@@
#                       ?מהו המספר הגדול ביותר מבין שניים
# המחשב מביא 2 מספרים אקראיים והשחקן כותב מהו המספר הגדול מבין השניים
# import random
# a=random.randint(1,100)
# b=random.randint(1,100)
# print(a,b)
# qu=int(input("\n? רתויב לודגה רפסמה "))

# if qu>a or qu>b:
#    print("\nדאמ הפי\n")
# else:
#     print("\nןוכנ אל \n")


#                   @@@          פעילות מספר 3        @@@
#                        ?מהו המספר הגדול ביותר מבין שלשה 
#המחשב מביא 3 מספרים אקראיים והשחקן כותב מהו המספר הגדול מבין השלשה

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

#                  @@@          פעילות מספר 3        @@@
#                       ?מהו המספר הגדול ביותר מבין שלשה 
#המחשב מביא 3 מספרים אקראיים והשחקן כותב מהו המספר הגדול מבין השלשה

# import random
# a=random.randint(1,100)
# b=random.randint(1,100)
# c=random.randint(1,100)
# print(a,b,c)
# qu=int(input("\n? רתויב לודגה רפסמה "))

# if a>b and a>c and qu==a:
#     print("\nדאמ ןוכנ")
# elif a>b and a<c and qu==c:
#     print("\nדאמ ןוכנ")
# elif a<b and b>c and qu==b:
#     print("\nדאמ ןוכנ")
# elif a<b and b<c and qu==c:
#     print("\nדאמ ןוכנ")
# elif qu!=a and qu!=b and qu!=c:
#     print("\nבוט האור אל התא")
# else:
#     print("\nהעוט התא")


# import random

# i=1
# while i<=5:
#     x=random.randint(1,10)
#     print(x)
#     i+=1
    
    