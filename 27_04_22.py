#מה התכנית מבצעת 
#1
# a = 4*256
# b = 8*128
# c = 16*64
# d = 32*32
# e = 2*512
# if a==b and a==c and a==d and a==e:
#     print("\n      equal")
# else:
#     print("\n      not equal")


#2
# name = "moti"
# if "i" in name:
#     print("\ni in ",name)
# else:
#     print("\ni is not in ",name)



#3
# name = "moti"
# letter = "t"
# if letter in name:
#     print("\n",letter, "in",name)
# else:
#     print("\n",letter,"is not in",name)


#להדגים הרצה של הקוד:מציג מספר דו ספרתי לפי ספרותיו
#4
# two_digits = int(input("\nenter a number of 2 digits "))
# asarot = int(two_digits/10)
# ahadot = two_digits-asarot*10
# print("Asarot digit = ",asarot,"\nAhadot digit = ",ahadot)


two_digits = int(input("\nenter a number of 2 digits "))
asarot = two_digits% 10
ahadot = two_digits-asarot*10
print("Asarot digit = ",asarot,"\nAhadot digit = ",ahadot)

