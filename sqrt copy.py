#@@@@@@@@@@@@@@@@@@@@@@@@@@משוואה ריבועית#@@@@@@@@@@@@@@@@@@@@@@@@@@@
import math
print("\n")
def sqr(a,b,c):
    Delta = (math.pow(b,2)-4*a*c)
    if Delta < 0:
        print(" "*8,"NO Solution\n")
    else:
        SQ = math.sqrt(Delta)
        X1 = (-b+SQ)/(2*a)
        X2 = (-b-SQ)/(2*a)
    if Delta == 0:   
        print(" "*8,"X12 = ",X1,"\n")
    elif Delta > 0:   
        print(" "*8,"X1 =",X1,"   X2 =",X2,"\n")

<<<<<<< HEAD
sqr(1,-5,-50)
=======
sqr(2,-10,-34)
>>>>>>> 84b3e099ed0b5b3661059206a322cbaaf8bd8073
       