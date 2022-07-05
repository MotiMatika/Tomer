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

# def sum_between_2(start,end):
#     # start = int(input("\nenter start : "))
#     # end = int(input("\nenter end : "))
#     A1 = start+1
#     An = end-1
#     n = end-start-1
#     Sn = (n*(A1+An)/2)
#     return Sn
# print("\nSn = ",sum_between_2(-2,2)) 

#אותה תכנית:מסכמת מספרים עוקבים בין 2 מספרים-ללא הקצוות
#start=0
#end=1
#a=start+1
#z=end-1
#kamut=end-start-1
#sum=((start+end)/2)*kamut
#print("\nThe sum of the numbers between",
#start,"and",end,"is",sum)

#אותה תכנית:מסכמת מספרים עוקבים בין 2 מספרים-כולל הקצוות
# start=3
# end=4
# kamut=end-start+1
# sum=((start+end)/2)*kamut
# print("\nThe sum of the numbers between",
# start,"and",end,"is",sum)

#print("He" + "l" * 2 + "o" + " Python " + str(7.2 / 2) + "." + str(3))
numbers = "123456789"

print(numbers[-1:-10])