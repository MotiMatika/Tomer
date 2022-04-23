#שתי הפונקציות הראשונות מחזירות מתוך שלשה אקראית את הגבוה
#הפונקציה השלישית מחזירה את המספר הגבוה מבין כל ה - 6
import random

a=random.randint(1,100)
b=random.randint(1,100)
c=random.randint(1,100)
print("\nthe first  threesome : ",a,b,c)
def biggest1_3(a,b,c):
    max_1 = max(a,b,c)
    return(max_1)
A=biggest1_3(a,b,c)

d=random.randint(1,100)
e=random.randint(1,100)
f=random.randint(1,100)
print("the second threesome : ",d,e,f)
def biggest4_6(d,e,f):
    max_2 = max(d,e,f)
    return(max_2)
B=biggest4_6(d,e,f)

def biggest1_6(A,B):
    maxx = max(A,B)
    return maxx
C=biggest1_6(A,B)
print("the biggest  of the 6 numbers is : ", C)