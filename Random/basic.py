
#הקוד מדפיס כמות אקראית של מספרים לפי הטוו שניתן לו
# import random
# num = random.randint(1,10)
# print("\n the random number is : ",num)
# for i in range(0,num):
#     print(i)

#2 הקודים הבאים מבצעים את אותה המשימה:
#סיכום מספרים עוקבים לפי טווח שהוגדר
#סיכום יחיד - מיקום פעולת ההדפסה
import random
num = random.randint(1,10)
print("\n the random number is : ",num)
sum = 0
for i in range(0,num):
    sum = sum+i
print(sum)


#סיכומי ביניים - מיקום פעולת ההדפסה
import random
num = random.randint(1,10)
print("\n the random number is : ",num)
sum = 0
for i in range(0,num):
    sum = sum+i
    print(sum)