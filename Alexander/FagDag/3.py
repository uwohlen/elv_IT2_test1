def fakultet(n):
    svar = n
    for x in range(n-1, 1, -1):
        svar *= x
    return svar

print(fakultet(5))