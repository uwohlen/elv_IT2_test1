from matplotlib import pyplot as plt


N = 100
f0 = 10
t0 = -5
time = 10

dt = time / (N - 1)

# få likning fra bruker

equation = input("dy/dx = ")

# oversett likningen til en funksjon

deriv = lambda x: eval(equation)

# sett opp listene for grafene

fderiv = [0] * N 
y = [0] * N
t = [0] * N

# sett startverdiene 

y[0] = f0
t[0] = t0

# kjør Eulers metode

for i in range(N - 1):
    fderiv[i] = deriv(t[i])
    y[i + 1] = y[i] + fderiv[i] * dt
    t[i + 1] = t[i] + dt
    
    
# plot grafene fra differensiallikningen    
    
plt.plot(t, y)

plt.show()
