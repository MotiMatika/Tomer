
                              #שתי הפונקציות הבאות ייכנסו לתוך פונקציית מיין
#def a(x):                 #הגדרת פונקציה
#	print(x+1)            #מוסיפה לקלט 1
#a(79)                     #קריאה לפונקציה + קלט

#import math               #ייבוא מספריית מאט

#def b(x):                 #הגדרת פונקציה
#	print(math.sqrt (x))  #העלאת קלט בחזקת 2
#b(64)                     #קריאה לפונקציה + קלט

#def name(x):
#	print(x)
#name("moti")

#def main():               #הגדרת פונקציית מיין
#	a()                   #הכללת פונקצייה איי
#	b()                   #הכללת פונקצייה איי
#	name()
#if __name__== "__a__":    #תחביר מורכב לביצוע כל 2 הפונקציות שכלולות במיין
#	main()#
#

                        #הפונקציה מחברת 2 מספרים
#def add(x,y):             #הגדרת הפונקציה עם 2 פרמטרים
#	"""adding 2 num"""    #תיעוד
#	print("x+y=",x+y)     #פלט
#add(1,2)                  #קריאה לפונקציה והשמת ערכים
#help(add)                 #קריאה לתיעוד של הפונקציה דרך הלפ

                        #הפונקציה מדפיסה מילה
#def words(prati,family):                 #הגדרת הפונקציה עם 2 פרמטרים
#	"""typing a word"""                  #תיעוד
#	print("the name is:",prati,family)   #פלט
#words("moti","yair")                     #קריאה לפונקציה והשמת ערכים
#help(words)                              #קריאה לתיעוד של הפונקציה דרך הלפ

                        #הפונקציה מחברת 2 מספרים
#def add(x,y):             #הגדרת הפונקציה עם 2 פרמטרים
#	"""adding 2 num"""    #תיעוד
#	t = x+y               #הסכום נכנס לתא טי
#	return t              #הפונקציה שומרת את הסכום

#a = add(8,2)              #קריאה לפונקציה והשמת ערכים לתא איי
#print("the sum is :",a)   #פלט של הסכום

                              #חלק זה מתרגל הבדלים בין משתנה לוקלי וגלובלי
#def word():             #הגדרת פונקציה
#	a = "moti"           #השמת ערך לתא איי
#	print(a)             #פלט
#word()                  #קריאה לפונקציה

#def word():      #הגדרת פונקציה
#	a = "moti"    #השמת ערך לתא איי
#	print(a)      #פלט
#print(a)         #יציאה מהפונקציה ובקשה לפלט איי שלא מוכר מחוץ לפונקציה
                  #נקבל הודעת שגיאה ניימארור

#def word():         #הגדרת פונקציה
#	a = "moti"      #השמת ערך לתא איי
#	print(a)        #פלט
#b = "yair"          #השמת ערך לתא בי - גלובלי
#print(b)            # פלט של תא בי
#word()              #קריאה לפונקציה שתדפיס את ערך איי הלוקלי

#def word():      #הגדרת פונקציה
#	a = "moti"   #השמת ערך לתא איי
#	print(a,b)   #פלט
#b = "yair"       #השמת ערך לתא בי - גלובלי
#word()           #קריאה לפונקציה שתדפיס את ערך איי הלוקלי וגם את בי הגלובלי שנכנס לפונקציה 





#import math
#def sr(a,b,c):
#	if delta1 < 0 or
#	x1 = (-b + math.sqrt(b**2-4*a*c))/2*a
#	x2 = (-b - math.sqrt(b**2-4*a*c))/2*a
#	print("a=",a,"  b=",b,"  c=",c)
#	print("the roots are:",x1,x2)
	
#sr(1,1,21)

                                  #חישוב שורשי משוואה ריבועית
# import math                                       #קריאה לספריית מאט
# def sr(a,b,c):                                    #הגדרת פונקציה עם 3 משתנים
# 	delta = b**2-4*a*c                            # הביטוי מתחת לשורש נכנס לתא דלתא
# 	if delta < 0:                                 #בדיקה האם דלתא קטנה מאפס
# 		print("a=",a,"  b=",b,"  c=",c)           #פלט -דיווח על המקדמים 
# 		print("It's a Math Error")                #פלט-הודעת שגיאה מתימטית-כי לא ניתן לחשב שורש של מספר שלילי
# 	else:	                                      #אחרת
# 		x1 = (-b + math.sqrt( delta))/2*a         #חישוב שורש ראשון
# 		x2 = (-b - math.sqrt( delta))/2*a         #חישוב שורש שני
# 		print("a=",a,"  b=",b,"  c=",c)           #פלט -דיווח על המקדמים
# 		print("The Roots are:",x1,x2)             #פלט -דיווח על השורשים
	
# sr(1,0,6) 


#from this import d


#def print123():
#    print("1")
#    print("2")
#    print("3")
#print123()

# מדפיס אותי
# def printMe():
#     print("Me!")


# def printCalculation(a,b):
#     c = a+b
#     print(c +3)
#     return c


# result = printCalculation(4,5)
# print("The result is: ", result)                                        #קריאה לפונקציה והשמת ערכים


#ארבע פונקציות שכל אחת מייצגת פעולה חשבונית בין שני מספרים
#פונקציית מיין שמאגדת את כל 4 הפונקציות

def plus(a,b):
    sum = a+b
    return sum


def minus(a,b):
    difference = a-b
    return difference


def multi(a,b):
    multi = a*b
    return multi


def divide(a,b):
    divide = a/b
    return divide


# def main():
    
#     #מסגרת
#     print("\n")
#     print("_"*20)
    
#     #קלט 2 מספרים
#     first_num  = int(input("Please enter #1 : ")) 
#     second_num = int(input("Please enter #2 : "))
#     print("_"*20)
    
#     #מסגרת
#     print("\n")
#     print("_"*40)
    
#     #פלט ע"י קריאה לפונקציות שלעיל 
#     print("The Sum      of the two numbers is :" ,plus  (first_num,second_num))
#     print("The Diffrence of the two numbers is :",minus (first_num,second_num))
#     print("The Product  of the two numbers is :" ,multi (first_num,second_num))
#     print("The Division of the two numbers is :" ,divide(first_num,second_num))
    
#     #מסגרת
#     print("_"*40)
#     print("\n")
    
# if __name__ == "__main__":
#     main()



#הפונקציה מחשבת ממוצע ציונים בהינתן לה רשימה של ציונים
# grades = [40,50,60,70,80,90]            #רשימת הציונים
# def average_grades(grades):
#     sum_grades=0                        #איתחול סכום הציונים
#     count=0                             #איתחול מניית כמות הציונים
#     for grade in grades:
#         sum_grades=sum_grades+grade     #סכום הציונים
#         count=count+1                   #מניית הציונים

#     av=sum_grades/count                 #חישוב הממוצע
#     return av
 
# print(average_grades(grades))

#רשימת של 6 ציונים אקראיים
# import random
# g1=random.randint(40,100)
# g2=random.randint(40,100)
# g3=random.randint(40,100)
# g4=random.randint(40,100)
# g5=random.randint(40,100)
# g6=random.randint(40,100)

# grades = [g1,g2,g3,g4,g5,g6]
# print(grades) 

# def average_grades(grades):
#     sum_grades=0                        #איתחול סכום הציונים
#     count=0                             #איתחול מניית כמות הציונים
#     for grade in grades:
#         sum_grades=sum_grades+grade     #סכום הציונים
#         count=count+1                   #מניית הציונים

#     av=sum_grades/count                 #חישוב הממוצע
#     return av
 
# print(average_grades(grades))

#לשפר את הקוד לאפשר לו לקרוא מקובץ אקסל ציונים ולבצע ממוצע


#פונקציה שמדפיסה  ציונים אקראיים כרשימה 
#ומדפיסה את:
# רשימת הציונים,את הציון הגבוה,הנמוך והממוצע   
# import random

# list=[]
# sum=0
# i=1

# num_test=int(input("\nWhat is the number of tests you have ?: "))
# while i<=num_test:
#         grade=random.randint(40,100)
#         sum=sum+grade
#         list.append(grade)
#         list.sort()
#         i+=1
# print("The grades are: ",list)
# print("The highest grade is: ",list.pop(num_test-1))
# print("The lowest grade is : ",list.pop(0))
# print("The average of the",num_test,"tests is :",sum/num_test)
   
#איך הופכים את הקוד לפונקציות קטנות ומשלבים אותן בפונקציית מיין



#def list_of_grades():

# # def main():

    
# # if __name__ == "__main__":
# #     main()


#sidra hehbonit
#סכום איברים סמוכים

A1=int(input("A1="))
d=int(input("d="))
Sn=int(input("Sn="))
n=(Sn-2*A1+d)/(2*d)
print(n,n+1)
