# #הגדול מבין 3 מספרים
# # רק אם הם שונים
# #גירסה ראשונה
# a = input ("\na = ")
# b = input ("b = ")
# c = input ("c = ")
# if a>b: 
#     if a>c:
#         print("   a is the biggest ",a)
#     else:
#         print("   c is the biggest ",c)
# else:
#     if b>c:
#         print("   b is the biggest ",b)
#     else:
#         print("   c is the biggest ",c)
 

#הגדול מבין 3 מספרים
# רק אם הם שונים
#גירסה שניה
# a = input ("\na = ")
# b = input ("b = ")
# c = input ("c = ")
# if a>b and a>c:
#     print("   1a is the biggest ",a)    
# if a>b and a<c :
#     print("   c is the biggest ",c)  
# if a<b and b>c:
#     print("   b is the biggest ",b)  
# if a<b and b<c:
#     print("   c is the biggest ",c) 

#הגדול מבין 3 מספרים
# רק אם הם שונים
#גירסה שלישית
# a = input ("\na = ")
# b = input ("b = ")
# c = input ("c = ")
# print("\nThe Biggest Number is : ",max(a,b,c)) 

#התכנית תמיין שלשה מספרים רק אם הם שונים
# a = input ("a = ")
# b = input ("b = ")
# c = input ("c = ")
# if a>b:
#     if a>c :
#         if b>c:
#             print(" "*5,"a > b > c\n"," "*4,a,">",b,">",c)
#         else:
#             print(" "*5,"a > c > b\n"," "*4,a,">",c,">",b)
#     else:
#         print(" "*5,"c > a > b\n"," "*4,c,">",a,">",b)
# else:
#     if b>c:
#         if a>c:
#            print(" "*5,"b > a > c\n"," "*4,b,">",a,">",c) 
#         else:
#             print(" "*5,"b > c > a\n"," "*4,b,">",c,">",a)
#     else:
#         print(" "*5,"c > b > a\n"," "*4,c,">",b,">",a) 