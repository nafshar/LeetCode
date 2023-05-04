def letterCombination(digits):
    # retyrn list[str]

    d_dict = {
        "1": [],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    if (len(digits) == 1 and digits[0] == "1"):
        return []

    if (len(digits) == 1):
        return d_dict.get(digits)
    ss = []
    for i in range(len(digits) - 1):
        for j in range(i+1, len(digits)):
            ss = ss + combo(d_dict.get(digits[i]), d_dict.get(digits[j]))
    return ss


def combo(l1, l2):
    cs = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            cs.append(l1[i] + l2[j])
    return cs


s = "213"
a = letterCombination(s)
print(a)
