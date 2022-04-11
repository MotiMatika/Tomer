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

#פונקציה שמקבלת מחרוזת ומזהה את המילה הארוע=כה ביותר
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

def absolute(num):
    if num >=0:
        print ("\nThe Absolute Number of ",num,"Is ",num)
    else:
        print("\nThe Absolute Number of ",num,"Is ",-num)
absolute(-3423)