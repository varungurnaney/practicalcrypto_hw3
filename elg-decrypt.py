import random
import sys 
import os
import math
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

f = open(sys.argv[1],"r")
lists = str(f.read()).split(",")
g_b = int(lists[0][1:])
ciphertext = lists[1][:-1]

#print(ciphertext)

f= open(sys.argv[2],"r")
lists = str(f.read()).split(",")
p = int(lists[0][1:])
g = int(lists[1])
a = int(lists[2][:-1])

g_a = pow(g,a,p)
g_ab = pow(g_b,a,p)

concatenated = str(g_a)+" "+str(g_b)+" "+str(g_ab)

#print(ciphertext)


key = hashlib.sha256(concatenated.encode()).digest()

aesgcm = AESGCM(key)

decrypted_text = aesgcm.decrypt(bytes.fromhex(ciphertext[0:32]),bytes.fromhex(ciphertext[32:]),None)
print(decrypted_text.decode("utf-8"))








