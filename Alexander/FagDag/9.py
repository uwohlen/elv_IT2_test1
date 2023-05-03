liste1 = [1,2,3,4,8,9,10,12,15,20]
liste2 = [1,5,9,20,100]


def flett(l1, l2):
    ret = []
    count1 = 0
    count2 = 0
    while len(ret) < (len(l1) + len(l2)):
        if l1[count1] < l2[count2]:
            ret.append(l1[count1])
            count1 += 1
        else:
            ret.append(l2[count2])
            count2 += 1
            
        if count1 == len(l1):
            for i in range(count2, len(l2)):
                ret.append(l2[i])
                
        if count2 == len(l2):
            for i in range(count1, len(l1)):
                ret.append(l1[i])
                
    return ret

print(flett(liste1, liste2))
                
                

