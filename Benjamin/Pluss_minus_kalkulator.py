z = input("Skriv inn ett pluss eller minus regnestykke med to tall: ") 

  

liste = list(z) 

o = z.replace(" ","") 

  

if "+" in o: 

   x = o.index("+") 

   p = int(o[0:x]) 

   k = int(o[x+1:]) 

   print(f' Svaret er = {p + k}') 

          

else: 

    x = o.index("-") 

    p = int(o[0:x]) 

    k = int(o[x+1:]) 

    print(f' Svaret er = {p - k}') 