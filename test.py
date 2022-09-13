def fun(s):
    subStrings = [""]

    for letter in s:

        letterAddedToSubString = False

        for i in range(len(subStrings)):

            if letter not in subStrings[i] and not letterAddedToSubString:
                subStrings[i] += letter
                letterAddedToSubString = True

        if not letterAddedToSubString:
            newSubString = letter
            subStrings.append(newSubString)
    print(subStrings)
    return len(subStrings)


def real(s):
    cnt, par = 0, ''
    for ch in s:
        print(par)
        if ch in par:
            cnt += 1
            par = ''
        par += ch
    return cnt + 1

print(fun("hdklqkcssgxlvehva"))
print(real("hdklqkcssgxlvehva"))


# "hdklqkcssgxlvehva"