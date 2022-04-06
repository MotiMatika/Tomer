#תרגיל 1

#משתמש מתבקש להקליד שלשה מספרים והתכנית בודקת אם יש בין המספרים , שני מספרים שווים
#אם היא מוצאת שני מספרים שווים היא מדפיסה : "מצאתי 2 מספרים שווים"
#אם היא לא מוצאת , היא מדפיסה: "לא מצאתי מספרים שווים"

# a = input ("\na = ")
# b = input ("b = ")
# c = input ("c = ")
# if a==b or a==c:
#     print("I found 2 equal numbers")
# else:
#     print("I didn't found any equal numbers")


#למקרה בו המשתמש מכניס 3 מספרים זהים

a = input ("\na = ")
b = input ("b = ")
c = input ("c = ")
if a==b and a==c:
    print("I found 3 equal numbers")
elif a==b or a==c:
    print("I found 2 numbers")
else:
    print("I didn't found any equal numbers")


#תרגיל 2
#המשתמש מתבקש להקליד שלשה מספרים 
# והתכנית בודקת מי המספר הקטן ביותר ומדפיסה
#  :"זהו המספר הקטן ביותר" 
# ואז היא רושמת את המספר הקטן ביותר.
# a = input ("\na = ")
# b = input ("b = ")
# c = input ("c = ")
# print("\nThe smallest Number is : ",min(a,b,c))




