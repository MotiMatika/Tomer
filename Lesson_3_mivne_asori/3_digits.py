#      @@@   פעילות 2  @@@
# פיצול מספר תלת ספרתי לספרותיו
# num = int(input("\nףלאל רשע ןיב רפסמ סנכה "))
# meot = int(num/100)
# print("תואמה תרפס  ",meot)
# asarot = int((num-meot*100)/10)
# print("תורשעה תרפס ",asarot)
# ahadot = int(num-100*meot-10*asarot)
# print("תודחאה תרפס ",ahadot)







briks=input("\nenter 3 digits - each for one pig "  )      #הכנסת מספר תלת ספרתי
pig1=int(int(briks)/100)                                 #הפרדת ספרת המאות שמציינת את מספר הלבנים שאסף חזיר ראשון
pig2=int((int(briks)/10-pig1*10))                        #הפרדת ספרת העשרות שמציינת את מספר הלבנים שאסף חזיר שני
pig3=int(briks)-(pig1*100+pig2*10)                       #הפרדת ספרת האחדות שמציינת את מספר הלבנים שאסף חזיר שלישי
sum=pig1+pig2+pig3                                       #חישוב סכום הלבנים שאספו שלשת החזירים
print("\nsum of briks collected :",sum)                    #הדפסת הסכום
get=int(sum/3)
print("\neach pig gets :", get," briks")                   #חלוקה שווה של הלבנים - ללא שארית
spare=sum-get*3
print("\nspare of brick after dividing :",spare)           # פלט לשארית שנותרה לאחר החלוקה
x=True
x=spare==0                                               #בודק האם יש שארית.שאלתי האם השארית שווה לאפס
print(x)  