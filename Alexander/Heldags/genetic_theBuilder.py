import random as rd

num_generations = 100
num_solutions = 10
num_best = 10
num_new_gen = 1000
satisfied = 9999
val_=50.0

def f(x,y,z):
    return 4*x**3-2*y**5+1/(1+z**2)

def fitness(x,y,z):
    ans = f(x,y,z)
    
    if ans==0:
        return 999999

    else:
        return float(abs(1/ans))

# Genereate solutions

solutions = []
for s in range(num_solutions):
    solutions.append((rd.uniform(-val_,val_),
                    rd.uniform(-val_,val_),
                    rd.uniform(-val_,val_))
                    )

#Take out the best 100 solutions
#num_generations = 1
for i in range(num_generations):
    ranked_solutions = []
    for s in solutions:
        fit = fitness( s[0],s[1],s[2] )
        ranked_solutions.append( (fit,s))
        #print(fit, s)

    ranked_solutions.sort()
    """
    for r in rankedsolutions:
        print(r)
    """
    ranked_solutions.reverse()
    #for r in ranked_solutions:
    #    print(r)
    
    print(f"=== Gen {i} best solutions ===")
    for j in range(1):
        #print("j = ",j,ranked_solutions[j])
        print(ranked_solutions[j])

    #make these cross over and mutate
    best_solutions = ranked_solutions[:num_best]
    if best_solutions[0][0]>=satisfied:
        break
    
    #Making a list for the next generation
    elements = []

    for s in best_solutions:
        elements.append(s[1])
       # elements.append(s[1][1])
        #elements.append(s[1][2])

    new_gen = []

    for _ in range(num_new_gen):
        """
        It woulc be great to have better control over the mutation size
        default now is plus/minus 5%

        Also, the crossing over seems to be random choices from every vaue of (x,y,z), 
        and it makes sense in a genetic algorithm. But it is equivalent to mixing genes for
        eye colour with genes for totalt body length, which does not make sense        
        """
        e1 = rd.choice(elements)[0] * rd.uniform(0.90,1.)
        e2 = rd.choice(elements)[1] * rd.uniform(0.90,1.10)
        e3 = rd.choice(elements)[2] * rd.uniform(0.90,1.10)

        new_gen.append((e1,e2,e3))

    solutions = new_gen
