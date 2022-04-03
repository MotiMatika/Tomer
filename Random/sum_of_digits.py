#הפונקציה מקבלת מספר אקראי ומסכמת את סכום ספרותיו
#אפשר לקבוע אם רוצים את טווח המספרים האקראיים

import random
num = random.randint(1,999)
print("\nThe random number is :",num)
def sum_digits(num):
    convert_num=str(num)
    length=len(convert_num)
    if length==1:
        sum = num
    elif length==2:
        asarot = int(num/10)
        ahadot = num-10*asarot
        sum    = asarot+ahadot
    else:
        meot   = int(num/100)
        asarot = int((num-100*meot)/10)
        ahadot = num-100*meot-10*asarot
        sum = meot+asarot+ahadot
    return sum
print("The sum of digits is :",sum_digits(num))