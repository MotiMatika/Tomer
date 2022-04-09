#קוד שמפרק את המילה לאותיות ורושם אותן כל אות בשורה חדשה
#for x in "banana":
#  print(x) 



#קוד שמסכם כמות איברים בטווח שניתן לו
# numbers = range(1,101)
# sum = 0
# for i in numbers:
#     sum +=i
# print("\nSum = ",sum)


#קוד שמדפיס את לוח הכפל של מספר 
# n=10
# for i in range(1,11):
#     print("\n",n,"x",i,"=",n*i)


#שני הקודים הבאים מפסיקים כאשר הם נתקלים במספר שלילי
#ההבדל ביניהם הוא הפלט-בגלל המיקום של הוראת print
#בקוד זה הפלט יהיה הערך האחרון של val שהוא המספר השלילי
numbers = [1,3,5,0,-4,10]
for val in numbers:
    if val<0:
        break
print(val)


#בקוד זה הפלט יהיה רשימת הערכים עד לערך השלילי
numbers = [1,3,5,0,-4,10]
for val in numbers:
    if val<0:
        break
    print(val)