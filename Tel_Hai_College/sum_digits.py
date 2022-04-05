def sum_digits(num):
    c=str(num)
    x=len(c)
    if x==1:
        sum = num
    elif x==2:
        asarot = int(num/10)
        ahadot = num-10*asarot
        sum    = asarot+ahadot
        #print(sum)
    else:
        meot   = int(num/100)
        asarot = int((num-100*meot)/10)
        ahadot = num-100*meot-10*asarot
        sum = meot+asarot+ahadot
        #print(sum)
    return sum
print(sum_digits(504))


