
#@@@@@@@@@@@@@@@@@@@@@@@@@@משוואה ריבועית#@@@@@@@@@@@@@@@@@@@@@@@@@@@
import math
#print("\n")
def sqr(a,b,c):
    Delta = (math.pow(b,2)-4*a*c)
    if Delta < 0:
        print("y=",a,"x^2+",b,"x+",c)
        print(" "*8,"NO Solution\n")
    else:
        sq = math.sqrt(Delta)
        x1 = (-b+sq)/(2*a)
        x2 = (-b-sq)/(2*a)
    if Delta == 0: 
        print("y=",a,"x^2+",b,"x+",c)  
        print("\n"," "*8,"X12 = ",x1,"\n")
    elif Delta > 0:
        print("y=",a,"x^2+",b,"x+",c)   
        print(" "*8,"X1 =",x1,"   X2 =",x2,"\n")


sqr(4,-132,1080)
       