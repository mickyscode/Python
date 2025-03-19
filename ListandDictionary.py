def converTodict(stringlist):
    dict={}
    stringlist=stringlist
    for word in stringlist:
        length=len(word)
        dict[word]=length
    return dict
def converTolist(dict):
    list=[]
    for i,j in dict.items():
        i=str(i)
        j=str(j)
        pair=i+" "+j
        list.append(pair)
    return list

def convertDistinctlist(list2):
    list3=[]
    for r in list2:
        if r  not in list3:
            list3.append(r)
    return list3

