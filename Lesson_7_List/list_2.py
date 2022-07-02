#  - מערך שיעור רשימות
#פעולות מתימטיות על רשימות
#1
# x=[1,2]
# print(x)                        #הצגת הרשימה-עם סוגריים מרובעים

# [1, 2]                    #פלט


#2
# x=[1,2]
# print(x*2)                        # הצגת הרשימה-עם סוגריים מרובעים - פעמיים כרשימה אחת

# [1, 2, 1, 2]              #פלט


#3
# x=[1,2]
# y=[3,4]
# print(x+y)                      #שילוב 2 הרשימות כרשימה אחת - עם סוגריים מרובעים

# [1, 2, 3, 4]              #פלט



#4
# x=[1,2]
# y=[3,4]
# print(x+y*2)                      #שילוב 2 הרשימות כרשימה אחת - עם סוגריים מרובעים אך רשימה וואי מוכפלת

# [1, 2, 3, 4, 3, 4]        #פלט


#5
# x=[1,2]
# y=[3,4]
# print((x+y)*2)  #                     #שילוב 2 הרשימות כרשימה אחת - עם סוגריים מרובעים מוכפלת

# [1, 2, 3, 4, 1, 2, 3, 4]  #פלט


#6
# x=[1,2]
# y=[3,4]
# z=[5,6]
# print(x+y+z)                    #שילוב 3 הרשימות כרשימה אחת - עם סוגריים מרובעים

# [1, 2, 3, 4, 5, 6]        #פלט


#לתרגל הכפלת כל רשימה וגם את כל הרשימות-סדר פעולות 7

#8
# x=[1,2]
# y=[3,4]
# z=[5,6]
# print(x[0]+y[0]+z[0])           #תוצאת חיבור האיברים

# 9                         #פלט



#9
# x=[1,2]
# y=[3,4]
# z=[5,6]
# print(x[0]*2+y[0]*3+z[0]/5)           #תוצאת תרגיל בין איברי הרשימות 

# 12.0                      #פלט



#10
# x=[1,2]
# y=[3,4]
# z=[5,6]
# print(2*(x[0]*2+y[0]*3+z[0]/5))        

# 24.0                      #פלט

#11
# x=[1,2]
# y=[3,4]
# z=[5,6]
# print(x[1],y[1],z[0])           #הצגת האיברים - ללא הסוגריים המרובעים

# 2 4 5                     #פלט


#12
# x=[1,2]
# y=[3,4]
# z=[5,6]
# print(x[0],y[1],z[2])           #הודעת שגיאה - מחוץ לתחום

# IndexError: list index out of range   #פלט

#13
# x=[1,2]
# y=[3,4]
# z=[5,6]
# print(2*(x[1]*2+y[1]*3+z[0]/5))   

# 34.0                  #פלט  

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




#14
# my_list=[1,2,3,4,5,6,7,8,9,10]
# e_zugi = my_list[0::2]   
# zugi=my_list[1::2]                           #שליפת כל ערך במקום זוגי ברשימה
# print(e_zugi)
# print(zugi)

# [1, 3, 5, 7, 9]                    #פלט
# [2, 4, 6, 8, 10]                   #פלט



#15
# my_list = [1,2,3,4,5,6,7,8,9,10]                    
# my_list.reverse()                               #הופך את סדר האיברים ברשימה
# print(my_list)

# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]     #פלט




#16
# my_list = [1,2,3,4,5,6,7,1,1,1,8,9,10]                    
# my_list.remove(1)                               #מסיר רק את ההופעה הראשונה של האיבר שצויין
# print(my_list)

# [2, 3, 4, 5, 6, 7, 1, 1, 1, 8, 9, 10]      #פלט


#17
# my_list = [7,2,9,4,6,5,1,8,3,10]                    
# my_list.sort()                                  #ממיין את סדר האיברים ברשימה
# print(my_list)

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#פלט




#18
# my_list = [1,2,3,4,5,6,7,1,1,1,8,9,10]                    
# my_list.pop(1)                                  #מסיר רק את האיבר במקום שצויין
# print(my_list)

[1, 3, 4, 5, 6, 7, 1, 1, 1, 8, 9, 10]      #פלט



#19
# my_list = [1,2,3,4,5,6,7,1,1,1,8,9,10]                    
# my_list.insert(0,5)                             #(5)מוסיף במקום המצויין (0) איבר נוסף
# print(my_list)

[5, 1, 2, 3, 4, 5, 6, 7, 1, 1, 1, 8, 9, 10] #פלט



#20
# my_list = [1,2,3,4,5,6,7,1,1,1,8,9,10]                    
# my_list.append(0)                               #(0)מוסיף לסוף הרשימה איבר נוסף
# print(my_list)

# [1, 2, 3, 4, 5, 6, 7, 1, 1, 1, 8, 9, 10, 0] #פלט



#21
# my_list = [1,2,3,4,5,6,7,1,1,1,8,9,10]                    
# my_list.clear()                                 #מרוקן את הרשימה 
# print(my_list)

# []   #פלט


#22
# my_list = [1,2,3,4,5,6,7,1,1,1,8,9,10]                    
# x = my_list.count(1)                            #מונה את כמות ההופעות של האיבר המצויין 
# print(x)

# 4   #פלט


#23
# my_list = [1,2,3,4,5,6,7,1,1,1,8,9,10]                    
# your_list = ["a","b"] 
# my_list.extend(your_list)                       #מוסיף רשימה שמצויינת לסוף רשימה ראשונה
# print(my_list)

# [1, 2, 3, 4, 5, 6, 7, 1, 1, 1, 8, 9, 10, 'a', 'b'] #פלט


#24
# x=[[7,5,2,1],[89]]#רשימה של רשימות ושליפת איבר מתוך רשימה
# print(x)
# print(x[0][1])                   

[[7, 5, 2, 1], [89]]  #פלט
5  #פלט



#25
# x=[[7,5,2,1],[89]]          #רשימה של רשימות ושליפת איברים מתוך הרשימות וביצוע פעולת חיבור ביניהם
# print(x)
# print(x[0][1]+x[0][3]+x[1][0])      

[[7, 5, 2, 1], [89]]    #פלט
95                      #פלט


# my_list = ["room","bed","stick","agg"]                    
# my_list.reverse()                             #הופך את הסדר של האיברים ברשימה
# print(my_list)




# my_list = ["farm","ear","bed","goal","car","dad","agg"]                    
# my_list.sort()                                  #ממיין את רשימת האיברים ברשימה בסדר אלפא-ביתי
# print(my_list)




# my_list = ["farm","ear","bed","goal","car","farm","dad","agg"]                    
# my_list.remove("farm")                           #מסיר רק את ההופעה הראשונה של האיבר שצויין
# print(my_list)




# my_list = ["farm","ear","bed","goal","car","farm","dad","agg"]
# print(my_list[0:2])




#קולטת 5 תווים,מחליטה אם הם הוקלדו בעבר,פולטת רשימה ללא כפילויות
# New_List = []
# for i in range(5):
#     char = input("Ente Your Guess : ")
#     if char in New_List:
#         print("           You already typed this letter")
#         New_List.sort()
#         print("The updated list is :",New_List)
#     else:
#         New_List.append(char)
#         New_List.sort()
#         print("The updated list is :",New_List)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@





# New_List = []
# for i in range(5):
#     char = input("Ente Your Guess : ")
#     if char in New_List:
#         print("         ** You already typed this letter")
#         New_List.sort()
#         print("The updated list is :",New_List)
#     else:
#         New_List.append(char)
#         New_List.sort()
#         print("The updated list is :",New_List)





# lst = [1, -15, 20] 
# x = max(lst)
# y = sum(lst)
# z = len(lst)
# result = min(x, y, z) 
# print(result)


#בקוד זה הפלט יהיה רשימת הערכים עד לערך השלילי
# numbers = [1,3,5,0,-4,10]
# for val in numbers:
#     if val<0:
#         break

#התכנית מחשבת ממוצע ציונים בהינתן לה רשימה של ציונים

# sum_grades=0
# count=0
# grades = [40,50,60,70,80]
# for grade in grades:
#     sum_grades=sum_grades+grade
#     count=count+1
# print(sum_grades)
# print(count)
# print("average= ",sum_grades/count)