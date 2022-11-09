tall = [21,19,9,10,43,42,54,4,7,8,9,1,12,7,6,445,432,999,77777,666]


len_tall = len(tall)

sortert = []

while len(sortert) < len_tall: 
    minste=tall[0]
    minste_index=0
    for x in range (len(tall)):
        
        if tall[x] < minste:

            minste=tall[x]
            minste_index=x

    tall.pop(minste_index)
    sortert.append(minste)            

print(sortert)