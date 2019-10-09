from random import randrange, getrandbits
import random
import sys 
import os
import math


def generate_prime_candidate(length):
    p = getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

def check_prime(n, k=128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def create_prime(length=1024):
    p = 4
    while not check_prime(p, 128):
        p = generate_prime_candidate(length)
   # print(p)
    return p

def first_n_digits(num, n):
    return num // 10 ** (int(math.log(num, 10)) - n + 1)

def modexp( base, exp, modulus ):
    return pow(base, exp, modulus)

def find_generator( p ):
    if p == 2:
        return 1

    p1 = 2
    p2 = (p-1) // p1
    while( 1 ):
        g = random.randint(2,5)
        if not (modexp( g, (p-1)//p1, p ) == 1):
                        if not modexp( g, (p-1)//p2, p ) == 1:
                                        return g

prime = create_prime()
g = find_generator(prime)
a = random.randint(2, prime-2)
g_a = pow(g,a,prime)



msg_to_bob = "("+str(prime)+","+str(g)+","+str(g_a)+")"
f = open(sys.argv[1],"w+") 
f.write(msg_to_bob) 

store_secret = "("+str(prime)+","+str(g)+","+str(a)+")"
f = open(sys.argv[2],"w+")
f.write(store_secret)






