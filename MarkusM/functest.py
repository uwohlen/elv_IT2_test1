class functs:
    def run():
        print("2")
    def a():
        print("a")

func = ("run","a","a")
for i in range(len(func)):
    getattr(functs,func[i])()

import matplotlib