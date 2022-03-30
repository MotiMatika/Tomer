# מציאת סכום האיברים בין 2 מספרים-ללא הגבולות שצויינו

# start = int(input("\nenter start : "))
# end = int(input("\nenter end : "))
# A1 = start+1
# An = end-1
# n = end-start-1
# Sn = (n*(A1+An)/2)
# print(" "*15,"Sn = ",Sn,"\n") 

#פונקציה שמבצעת בדיוק את המשימה של הקוד הקודם
#

def sum_between_2(start,end):
    # start = int(input("\nenter start : "))
    # end = int(input("\nenter end : "))
    A1 = start+1
    An = end-1
    n = end-start-1
    Sn = (n*(A1+An)/2)
    return Sn
print("\nSn = ",sum_between_2(2,4)) 
