#שלבים בבניית פונקציה

#הפונקציה ממתינה לקלט
#כשיהיה לה קלט היא תחזיר אותו-אם תהיה פקודת הדפסה
# def first_func(x):
#     return x
# first_func(4)
# print (first_func(3))

#הפונקציה ממתינה לקלט
#כשיהיה לה קלט היא תחזיר אותו-אם תהיה פקודת הדפסה
# def first_func(a):
#     return a    
# first_func(5)  #קריאה לפונקציה
# #לא יוחזר דבר

# def first_func(a):
#     return a    
# print(first_func(5))
# #יודפס הקלט

# def second_func(b):
#     return b

#ניתן להשתמש בתוצרים של הפונקציות לפעולות בין הפונקציות
# x = first_func(2) + second_func(8)
# print(x)

# y = first_func(3) * second_func(2)
# print(y)

#או בדרך אחרת
#להכניס תוצר של כל פונקציה למשתנה אחר -ואז לבצע פעולות
# x = first_func(4)
# y = second_func(5)
# print(x+y)







# import random
# a=random.randint(1,100)
# b=random.randint(1,100)
# c=random.randint(1,100)


#מהו המספר הגדול ביותר מבין שלשה
# def out_of_three(a,b,c):
#     print("\n",a,",",b,",",c)
#     qu=int(input("\n? רתויב לודגה רפסמה "))

#     if a>b and a>c and qu==a:
#         print("\nדאמ ןוכנ")
#     elif a>b and a<c and qu==c:
#         print("\nדאמ ןוכנ")
#     elif a<b and b>c and qu==b:
#         print("\nדאמ ןוכנ")
#     elif a<b and b<c and qu==c:
#         print("\nדאמ ןוכנ")
#     elif qu!=a and qu!=b and qu!=c:
#         print("\nבוט האור אל התא")
#     else:
#         print("\nהעוט התא")
#     # out_of_three(2,4,1)

# out_of_three(a,b,c)

#פונקציה שמקבלת מחרוזת ומזהה את המילה הארוכה ביותר
# def lon_word(text):
#     num_of_words = text.split()
#     print(num_of_words)
#     last_length = 1
#     for i in num_of_words:
#         new_length = len (i)
#         if new_length>last_length:
#             last_length = new_length
#             longest_word = i
#     return longest_word
#     #print(longest_word)

# print(lon_word("today is friday"))


#פונקציה שמקבלת מספר ומדפיסה את הערך המוחלט שלו
#אפשר גם גירסה למספר אקראי
# def absolute(num):
#     if num >=0:
#         print("\nThe Absolute Number of ",num,"Is ",num)
#     else:
#         print("\nThe Absolute Number of ",num,"Is ",-num)
# absolute(-3423)

# def greeting(name):
#     print("\nHello",name,".","How are you ?")
# greeting("moti")





