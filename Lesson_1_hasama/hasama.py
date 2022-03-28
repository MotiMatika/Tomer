# # print(1+2)
# # print(100/10)
# # print("tomer")
# # print("*     "*5)



# # a=3
# # b=5
# # print(a+b)
# # print(3*a)
# # print(b-4)
# # print(a*(b-a))
# # print(3*a+2*b)


# # a="tomer "
# # b="shifman"
# # print(a,b)
# # c="hilla"
# # print(c,b)
# # print(a*39)

# print("2+3")
# print(2+3)
# print("2+3 = ",5)


#המשתמש מקליד את גילו בשנים ומקבל את גילו בחודשים
years = int(input("\ntype your age in years: "))
months = years*36
print("your age in months : ",months)

#פעילויות נוספות: להמיר לשבועות,ימים,דקות,שניות


#משתמש מכניס מספר ופלט : שמו נכתב מספר הפעמים שהכניס
times = int(input("\ntype a number you your name to be print: "))
name = input("\ntype your name : ")
print(times*name)







# briks=input("enter 3 digits - each for one pig "  )      #הכנסת מספר תלת ספרתי
# pig1=int(int(briks)/100)                                 #הפרדת ספרת המאות שמציינת את מספר הלבנים שאסף חזיר ראשון
# pig2=int((int(briks)/10-pig1*10))                        #הפרדת ספרת העשרות שמציינת את מספר הלבנים שאסף חזיר שני
# pig3=int(briks)-(pig1*100+pig2*10)                       #הפרדת ספרת האחדות שמציינת את מספר הלבנים שאסף חזיר שלישי
# sum=pig1+pig2+pig3                                       #חישוב סכום הלבנים שאספו שלשת החזירים
# print("sum of briks collected :",sum)                    #הדפסת הסכום
# get=int(sum/3)
# print("each pig gets :", get," briks")                   #חלוקה שווה של הלבנים - ללא שארית
# spare=sum-get*3
# print("spare of brick after dividing :",spare)           # פלט לשארית שנותרה לאחר החלוקה
# x=True
# x=spare==0                                               #בודק האם יש שארית.שאלתי האם השארית שווה לאפס
# print(x)      