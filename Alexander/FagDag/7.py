kø = []
stakk = []

def push_kø(obj):
    kø.append(obj)
    
def pop_kø():
    ret = kø[0]
    kø.remove(ret)
    return ret

def push_stakk(obj):
    stakk.append(obj)
    
def pop_stakk():
    ret = stakk[-1]
    stakk.pop()
    return ret


    