
#הקוד מדפיס כמות אקראית של מספרים לפי הטווח שניתן לו
# import random
# num = random.randint(1,10)
# print("\n the random number is : ",num)
# for i in range(0,num):
#     print(i)

#2 הקודים הבאים מבצעים את אותה המשימה:
#סיכום מספרים עוקבים לפי טווח שהוגדר
#סיכום יחיד - מיקום פעולת ההדפסה
# import random
# num = random.randint(1,10)
# print("\n the random number is : ",num)
# sum = 0
# for i in range(0,num):
#     sum = sum+i
# print(sum)


#סיכומי ביניים - מיקום פעולת ההדפסה
# import random
# num = random.randint(1,10)
# print("\n the random number is : ",num)
# sum = 0
# for i in range(0,num):
#     sum = sum+i
#     print(sum)

#הקוד מריץ מספרים אקראיים וקובע אם המספר זוגי או אי-זוגי
# import random
# num = random.randint(1,100)
# print("\n"*5,"The Random number is :",num)
# if num%2 == 0:
#     print("\n"*2,num,"is pair")
# else:
#     print("\n"*2,num,"is not a pair")


#להדגים הרצה של הקוד:מציג מספר דו ספרתי לפי ספרותיו
#4
# two_digits = int(input("\nenter a number of 2 digits "))
# asarot = int(two_digits/10)
# # print(asarot)
# ahadot = two_digits-asarot*10
# print("Asarot digit = ",asarot,"\nAhadot digit = ",ahadot)




# two_digits = int(input("\nenter a number of 2 digits "))
# asarot = two_digits//10
# ahadot = two_digits% 10
# print("Asarot digit = ",asarot,"\nAhadot digit = ",ahadot)

#התוצר
# enter a number of 2 digits 54
# Asarot digit =  5 
# Ahadot digit =  4

# x=9//2
# print(x)

# x=8//3
# print(x)

# x=4//2
# print(x)



# print(4//2)

print("\nthis is asarot digit",76//10)
print("this is ahadot digit",76%10)