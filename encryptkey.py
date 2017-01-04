import primenos
import random

def modcondcheck(eXd,totient):
    if (eXd - 1) % totient == 0:
        return True
    else:
        return False
def genkey():
    r = primenos.primenos()
    p = random.choice(r)
    q = random.choice(r)
    print p, q

    n = p*q

    t = (p - 1) * (q - 1)
    e = 0
    flag = False

    while not flag:
        e = random.randint(1,t)
        flag = primenos.coprime(e,t)

    d = 0
    while True:
        d = random.randint((2**20),(2**30))
        if (modcondcheck(e*d,t)):
            break

    print "Totient     = ", t
    print "Public Key  = (",n,",",e,")"
    print "Private Key = ",d

    return(n,e,d)
