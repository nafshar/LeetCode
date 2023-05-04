
def com(ochar, startIndex, endIndex):
    char = ochar[startIndex:endIndex]
    compartments = []
    products = []
    ci = find(char, "|")
    if len(ci) > 1:
        j=1
        for i in range(len(ci)-1):
            compartments.append(j)
            products.append(ci[i+1]-ci[i]-1)
            j += 1
    pairs = list(zip(compartments, products))
    return pairs


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
