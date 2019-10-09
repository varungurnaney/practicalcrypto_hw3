import os 
import sys
import random 

f = open(sys.argv[1],"r")
lists = str(f.read()).split(",")
p = int(lists[0][1:])
g = int(lists[1])
ga_modp = int(lists[2][:-1])

for i in range(2,p-2): 
	if pow(g,i,p) == ga_modp: 
		print(i)
		break



