summ = input("Summen: ")

# passer på at hvis første tallet er negativt ødelegger det ikke for + - søkesystemet

if summ[0] == '-':
    summ2 = summ[1:]
else:
    summ2 = summ

# leter etter string index for + eller - tegnet
plus = summ2.find("+")
minus = summ2.find("-")

# .find() metoden vil returnere -1 hvis det finnes ikke det tegnet i stringen

if plus != -1:
    # summerer tallene før + tegnet og etter + tegnet
    out = int(summ[:plus]) + int(summ[(1 + plus):])
    print(out)
elif minus != -1:
    out = int(summ[:minus]) - int(summ[(1 + minus):])
    print(out)
else:
    print("Invalid input!!!")
    
    
    
    
    
    