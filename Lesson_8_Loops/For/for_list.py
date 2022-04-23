# list = ["a","b","c","d"]
# for i in list:
#     print(i)



#2 הקודים הבאים מבצעים אותה משימה
#ההבדל-מיקום פעולת ההדפסה
#פעולת ההדפסה בפנים
# list = ["a","b","c","d"]
# for i in list:
#     if i=="a":
#         print(i)
#     else:
#         print("no")

#פעולת ההדפסה בחוץ
# list = ["a","b","c","d"]
# for i in list:
#     if i=="a":
#         print(i)
# print("no")

#לא מבצע דבר כי לא מוצא את t ברשימה
# list = ["a","b","c","d"]
# for i in list:
#     if i=="t":
#         print(i)


#מדפיס את האות האחרונה
# list = ["a","b","c","d"]
# for i in list:
#     if i=="t":
#         break
# print(i)


#פונקציה שמחפשת באופן סידרתי איבר ברשימה
# list = [1,2,3,4,5,6]
# num = 13
# def search(list,num):
#     for i in list:
#         if i == num:
#             return True
        
#     return False 

# print(search(list,num))




list = [1,2,3,4,5,6]
num = 3
def binary_search(list,nun):
    left = 0
    right = len(list)-1
    while left<=right:
        mid = (left+right)//2
        if num == list[mid]:
            return True
        else:
            if num<list[mid]:
                right=mid-1
            else:
                left = mid+1
    return False
print(binary_search(list,num))




