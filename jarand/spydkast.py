deltaker_1 = ["Per" , 4,1,2,2]
deltaker_2 = ["Lise" , 5,2,3,1]
deltaker_3 = ["Simen" , 5,2,3,2]

resultat = [deltaker_1,deltaker_2,deltaker_3]


def sort(list):
    for x in range (len(list[0])):
        index_list = 1
        for i in range(len(list[0])-1):
            print(index_list)
            if list[1][index_list]<list[1][index_list+1]:
                list[1][index_list], list[1][index_list+1]= list[1][index_list+1], list[1][index_list]
            index_list=i+1
    # for x in range (len(list)):
    #     index_list = 0
    #     for i in range(len(list)):
    #         if list[index_list][1]>list[index_list+1][1]:
    #             list[index_list][1], list[index_list+1][1]= list[index_list+1][1], list[index_list][1]
    #         index_list=i
    return(list)

sort(resultat)

print (deltaker_2)
