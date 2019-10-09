import random
import sys 
import os
import math

f = open(sys.argv[1],"r")

g_b = int(f.read())

f = open(sys.argv[2],"r")

lists = str(f.read()).split(",")

a = int(lists[2][:-1])

p = int(lists[0][1:])

g_ab = pow(g_b,a,p)

print(g_ab)

