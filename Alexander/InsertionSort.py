
array = [23, 2, 56, 7, 33, 1, 6, 5, 8, 3]


def insert(i, x, array):
    tmp = array[x]
    del array[x]
    array.insert(i, tmp)

def insertionSort(array):
    for x in range(1, len(array)):
        tmp = array[x]
        if tmp < array[x - 1]:
            for i in range(x - 1, -1, -1):
                if i == 0:
                    insert(i, x, array)
                    break
                if tmp < array[i] and tmp >= array[i - 1]:
                    insert(i, x, array)
                    break
    return array
                    
array = insertionSort(array)
print(array)
