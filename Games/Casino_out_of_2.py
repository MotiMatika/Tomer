import random
#אקראיות בבחירת מספר.לספור מי ניצח אקראית את השני
moti = random.randint(1,100)
print("\nmoti ,your number is    :",moti)
some_one = random.randint(1,100)
print("\nsome_one,your number is :",some_one)

if moti > some_one:
    print("\n     ***********")
    print("     * M O T I *")
    print("     ***********")
else :
    print("\n*******************")
    print("* S O M E _ O N E *")
    print("********************")


#יש המשך-גירסא נוספת

#  







import random
#אקראיות בבחירת מספר.לספור מי ניצח אקראית את השני
moti = random.randint(50,100)
print("\nmoti ,your number is    :",moti)
some_one = random.randint(1,40)
print("\nsome_one,your number is :",some_one)

if moti > some_one:
    print("\n     ***********")
    print("     * M O T I *")
    print("     ***********")
else :
    print("\n*******************")
    print("* S O M E _ O N E *")
    print("********************")