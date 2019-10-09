import random
import sys 
import os
import math

f = open(sys.argv[1],"r")
lists = str(f.read()).split(",")
p = int(lists[0][1:])
g = int(lists[1])
g_a = int(lists[2][:-1])

b = random.randint(2, p-2)

g_b = pow(g,b,p)

f = open(sys.argv[2],"w+")
f.write(str(g_b))

g_ab = pow(int(g_a),b,p)
print(str(g_ab))

