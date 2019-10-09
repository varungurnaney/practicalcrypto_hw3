import random
import sys 
import os
import math
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

message = sys.argv[1]
f = open(sys.argv[2],"r")
lists = str(f.read()).split(",")
p = int(lists[0][1:])
g = int(lists[1])
g_a = int(lists[2][:-1])


b = random.randint(2, p-2)
g_b = pow(g,b,p)
g_ab = pow(g_a,b,p)

concatenated = str(g_a)+" "+str(g_b)+" "+str(g_ab)

key = hashlib.sha256(concatenated.encode()).digest()

#ciphertext = encrypt(key,bytes(message,'utf-8'),None)

#print(ciphertext)

aesgcm = AESGCM(key)
iv = os.urandom(16)
#print(iv.hex())
ciphertext = (aesgcm.encrypt(iv,bytes(message,'utf-8'),None)).hex()
#print(ciphertext)
store_secret = "("+str(g_b)+","+str(iv.hex())+str(ciphertext)+")"
f = open(sys.argv[3],"w+")
f.write(store_secret)








