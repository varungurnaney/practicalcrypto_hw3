from math import ceil, sqrt
import sys
import random 

def baby_step_giant_step(g, h, p):
    N = ceil(sqrt(p - 1)) 
    tbl = {pow(g, i, p): i for i in range(N)}
    c = pow(g, N * (p - 2), p)
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]
    return None



f = open(sys.argv[1],"r")
lists = str(f.read()).split(",")
p = int(lists[0][1:])
g = int(lists[1])
ga_modp = int(lists[2][:-1]) 

print(baby_step_giant_step(g,ga_modp,p))