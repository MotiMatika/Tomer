
#הגדול מבין 2 מספרים 
# רק אם הם שונים
#גירסה ראשונה
# a = int(input ("\na = "))
# a = int(input ("b = "))
# if a>b:
#     print(a,">",b)
# else:
#     print(b,">",a)

#הגדול מבין 2 מספרים 
# רק אם הם שונים
#גירסה שניה
# a = int(input ("\na = "))
# b = int(input ("b = "))
# print("The Biggest Numbe is : ",max(a,b))



#ממיינת בין 2 מספרים מי גדול יותר גם אם הם שווים

# a = int(input ("a = "))
# b = int(input ("b = "))
# if a>b:
#     print(a,">",b)
# elif a==b:
#     print(a,"=",b)
# else:
#     print(b,">",a)

#מזהה את האות שבאה אחרי האות האחרת
a = input ("first letter = ")
b = input ("second letter = ")
if a>b:
    print(a,"comes after",b)
elif a==b:
    print(a,"it's the same letter as",b)
else:
    print(b,"comes after",a)