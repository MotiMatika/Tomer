#הפונקציה מקבלת מספר אקראי ומסכמת את סכום ספרותיו
#אפשר לקבוע אם רוצים את טווח המספרים האקראיים
# רק למספר תלת ספרתי
# import random
# num = random.randint(1,999)
# print("\nThe random number is :",num)
# def sum_digits(num):
#     convert_num=str(num)
#     length=len(convert_num)
#     if length==1:
#         sum = num
#     elif length==2:
#         asarot = int(num/10)
#         ahadot = num-10*asarot
#         sum    = asarot+ahadot
#     else:
#         meot   = int(num/100)
#         asarot = int((num-100*meot)/10)
#         ahadot = num-100*meot-10*asarot
#         sum = meot+asarot+ahadot
#     return sum
# print("The sum of digits is :",sum_digits(num))



# הקוד מסכם ספרותיו של מספר אקראי                                
# דרור   9.4.22                                 
import random
number = random.randint(1,10000)
def sum_int(number):
    print(number)
    sum = 0
    while number != 0:
        sum = sum + number % 10   #מודולו משאיר את השארית לאחר החילוק ב 10
        number = number // 10# הפעולה // לוקחת את התוצאה השלמה לאחר חילוק ב 10     
    return sum

print(sum_int(number))










