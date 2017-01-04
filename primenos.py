#Eratosthenes Seive

def primenos():
    N = 10000
    r = [2]
    l = range(2,N)

    for m in r:
        for n in l:
            if n % m == 0:
                l.remove(n)
        if(len(l) != 0):
            r.append(l[0])

    r.extend(l)
    return r

def coprime(a,b):
    l = range(2,a+1)
    for i in l:
        if (a % i) == 0 and (b % i) == 0:
            return False
    return True
            


