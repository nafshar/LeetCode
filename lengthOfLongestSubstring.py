def llss (s) :
    st = []
    for letter in s:
        st.append(letter)
    i = 0
    st1 = []
    lcl = []
    while i < len(st):
        if (st[i] not in st1):
            st1.append(st[i])
        elif (len(st1) >= len(lcl)):
            # copy st1 into lcl and start a new substring
            lcl = st1[:]
            # keep all in st1 up to the duplicate
            dupindex = st1.index(st[i])
            st1 = st1[dupindex+1:]
            st1.append(st[i])
        else :
            # keep all in st1 up to the duplicate
            dupindex = st1.index(st[i])
            st1 = st1[dupindex + 1:]
            st1.append(st[i])
        i += 1

    # now we need to check if the last st1 is the longest
    if (len(st1) > len(lcl)):
        # copy st1 into lcl and start a new substring
        lcl = st1[:]

    # convert the list back to a string
    rs =''
    for char in lcl:
        rs += char
    return rs

s = " "
sub = llss(s)
print("sub = ", sub)
print("sub length = {}".format(len(sub)))