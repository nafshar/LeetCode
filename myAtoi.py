import numpy as np

def myAtoi(s):
    try:
        s = s.strip()
    except TypeError:
        s = np.unicode.strip(s)

    i=0
    negative = False
    if s[0] == "-":
        negative = True
        i=1
    elif s[0] == "+":
        negative = False
        i=1


    #parse the digits
    ss = ""
    while i <= len(s)-1 and s[i].isdigit():
        ss = ss+str(s[i])
        i += 1

    if ss == "":
        return 0

    # We have some digits
    try:
        numeric_filter = filter(str.isdigit, ss)
    except TypeError:
        numeric_filter = filter(np.unicode.isdigit, ss)
    numeric_string = "".join(numeric_filter)
    intvalue = int(numeric_string)

    if negative:
        intvalue *= -1

    if(intvalue < -(2**31)) :
        intvalue = -2**31
    elif(intvalue > (2**31 -1)) :
        intvalue = 2**31 -1

    return intvalue

#s="  -4193 with words"
#s = "words and 987"
#s = "-91283472332"
#s="3.14159"
#s="-+42"
intv = myAtoi(s)
print (intv)