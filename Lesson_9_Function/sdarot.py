#סכום כל המספרים  
# a1 = int(input("\nstart: "))
# an = int(input("end: "))
# n = an-a1+1
# sn = n*(2*a1+n-1)/2
# print("The Sum of",n,"numbers is: ",sn)

#כמות האיברים החיוביים
a1 = int(input("\na1: "))
d = int(input("d: "))
n = int((d-a1)/d)
print("There are ",n,"positive numbers")
an = a1 + d*(n-1)
if an == 0:
    an = an-d
print("The last positive number is:",an)