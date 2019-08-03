def useAlp(FILE = ""):
    inf = {}
    ALP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '-,.;"
    for i in range(len(ALP)):
        tmp = 0
        for j in range(len(FILE)):
            if (ALP[i] == FILE[j]):
                tmp += 1
        inf[ALP[i]] = tmp
        tmp = 0
    return inf

def dictSorted(inf = {}, type = True):
    if(type == True):
        infSorted = (sorted(inf.items(), key= lambda x: x[1], reverse=True))
        dinfSorted = {}
        for i in range(len(infSorted)):
            tmp = infSorted[i]
            dinfSorted[tmp[0]] = tmp[1]
        return dinfSorted
    else:
        infSorted = (sorted(inf.items(), key= lambda t : t[0]))
        dinfSorted = {}
        for i in range(len(infSorted)):
            tmp = infSorted[i]
            dinfSorted[tmp[0]] = tmp[1]
        return dinfSorted

def nGram(FILE, step = 2):
    my_list = []
    for j in range(len(FILE)):
        temp = FILE[j:j + step]
        if " " not in temp:
            if "\n" not in temp:
                if temp not in my_list:
                    my_list.append(temp)
    nGramDict = {}
    for i in range(len(my_list)):
        temp = 0
        for j in range(len(FILE)):
            if (j != len(FILE) - 1):
                tempNg = FILE[j:j + step]
                if (my_list[i] == tempNg):
                    temp += 1
        nGramDict[my_list[i]] = temp
        temp = 0
    return nGramDict