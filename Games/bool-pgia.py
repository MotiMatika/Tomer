###########################################בול-פגיעה################
#שחקן מנחש מספר אקראי בן 4 ספרות
#משחק נגד המחשב

#הפונקציה שמקבלת מספר אקראי לניחוש השחקן
#הפונקציה מפרקת את המספר האקראי לספרותיו

import random as rd
com_num = rd.randint(10,99)
print(com_num)
def ran_num(num_to_guess):
    guess_asarot = num_to_guess//10
    guess_ahadot = num_to_guess% 10
    return guess_asarot,guess_ahadot
     
print(ran_num(com_num))



#הפונקציה שמפרקת את הניחוש לספרות
def user_num(two_digits):
    #two_digits = int(input("\nenter a number of 2 digits "))
    asarot = two_digits//10
    ahadot = two_digits% 10
    return asarot,ahadot
    
print(user_num(56))

if ran_num==two:
    print("bool")
else:
    print("pgia")