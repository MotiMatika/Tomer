''' hello '''
## sidra hehbonit
#
# סכום כל המספרים
# a1 = int(input("\nstart: "))
# an = int(input("end: "))
# n = an-a1+1
# sn = n*(2*a1+n-1)/2
# print("The Sum of",n,"numbers is: ",sn)

# כמות האיברים החיוביים בסידרה יורדת
# a1 = int(input("\na1: "))
# d = int(input("d: "))
# n = int((d-a1)/d)
# print("There are ",n,"positive numbers")


#מציאת האיבר החיובי האחרון
a1 = int(input("\na1: "))
d = int(input("d: "))
n = int((d-a1)/d)
an = a1 + d*(n-1)
if an == 0:
    an = an-d
print("The last positive number is:",an)

# מיקום זוג איברים סמוכים כאשר נתון סכומם   

# A1=int(input("A1="))
# d=int(input("d="))
# Sn=int(input("Sn="))
# n=(Sn-2*A1+d)/(2*d)
# print(n,n+1)
