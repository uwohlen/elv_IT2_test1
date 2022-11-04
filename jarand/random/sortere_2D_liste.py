

deltaker_1 = ["Per" , 3]
deltaker_2 = ["Lise" , 2]
deltaker_3 = ["Simen" , 1]

resultat = [deltaker_1,deltaker_2,deltaker_3]

def sort(list):
    for x in range (len(list)):
        index_list = 0
        for i in range(len(list)):
            if list[index_list][1]>list[index_list+1][1]:
                list[index_list][1], list[index_list+1][1]= list[index_list+1][1], list[index_list][1]
            index_list=i
    return(list)

sort(resultat)

print (resultat)