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













#אפשר לרמות - ותמיד לנצח
# moti = random.randint(10,11)
# print("moti ,your number is :",moti)
# pupil = random.randint(10,80)
# print("pupil,your number is :",pupil)