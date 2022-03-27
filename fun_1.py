

#מהו המספר הגדול ביותר מבין שלשה
def out_of_three(a,b,c):
    # import random
    # a=random.randint(1,100)
    # b=random.randint(1,100)
    # c=random.randint(1,100)
    print("\n",a,",",b,",",c)
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
    # out_of_three(2,4,1)

out_of_three(2,4,1)