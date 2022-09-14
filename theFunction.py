
def theReverse(list=[]):
    """tar en liste og reverser det tilbake """

    if list is None:
        list = []
    resList=[]
    for i in range(0,len(list)):
        ind=len(list)-i-1
        resList.append(1)
        resList[i]=list[ind]
    return resList

l=[1,4,2,5,8,7]

print(theReverse(l),"   ",l)
