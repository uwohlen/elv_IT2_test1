def search(query, array):
    """binært søkealgoritme for lister av tall som er i riktig rekkefølge"""
    lst = array.copy()
    waste = []
    while True:
        try:
            middle = len(lst) // 2
            if lst[middle] == query:
                return len(waste) + middle
            elif lst[middle] < query:
                waste += lst[:middle + 1]
                del lst[:middle + 1]
            else:
                del lst[middle:]
        except:
            return "No Value Found!!!"
