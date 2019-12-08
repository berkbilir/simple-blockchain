from Crypto.PublicKey import DSA
import random
import string
import os.path
import Crypto
from Crypto.Hash import SHA3_256
from Crypto.Util import number
import warnings
import pyprimes


#Berk Bilir 23621
#Doğukan Köksal 24305

def random_prime(bitsize):
    warnings.simplefilter('ignore')
    chck = False
    while chck == False:
        p = random.randrange(2**(bitsize-1), 2**bitsize-1)
        chck = pyprimes.isprime(p)
    warnings.simplefilter('default')    
    return p

def large_DL_Prime(q, bitsize):
    warnings.simplefilter('ignore')
    chck = False
    while chck == False:
        k = random.randrange(2**(bitsize-1), 2**bitsize-1)
        p = k*q+1
        chck = pyprimes.isprime(p)
    warnings.simplefilter('default')    
    return p

def Param_Generator(qsize, psize):
    q = random_prime(qsize)
    p = large_DL_Prime(q, psize-qsize)
    tmp = (p-1)//q
    g = 1
    while g == 1:
        alpha = random.randrange(1, p)
        g = pow(alpha, tmp, p)
    return q, p, g

def GenerateOrRead(file):
	if os.path.isfile(file):
		
		f = open(file, "r")
		q = int(f.readline())
		p = int(f.readline())
		g = int(f.readline())
		f.close()

		return(q,p,g)
	
	else:
		
		#TODO

		(q,p,g) = Param_Generator(224,2048)

		f = open(file,"w")
		f.write(str(q)+"\n")
		f.write(str(p)+"\n")
		f.write(str(g))
		f.close()
    	
		return(q,p,g) 


	

def random_string(size=6, chars=string.ascii_uppercase + string.ascii_lowercase+ string.digits):
    return ''.join(random.choice(chars) for x in range(size))

#Normalde ya kendimiz generate etmemiz gerekiyo ama eğer kullanıcı kendi değer vermek istiyosa pubparams.txt yi kullanabilir. 
#Kendi generate etme kısmı setup() fonskiyonuna eklenmeli
def Setup():
	if os.path.isfile("pubparams.txt"):
		
		f = open("pubparams.txt", "r")
		q = int(f.readline())
		p = int(f.readline())
		g = int(f.readline())
		f.close()

	return(q,p,g)



def KeyGen(q,p,g):
	
	alpha = random.randrange(0, q -1)
	beta = pow(g, alpha, p)

	return alpha,beta


def SignGen(m,q,p,g,alpha):

	#m = m.decode('utf-8')

	h = SHA3_256.new()

	h.update(m)

	bebe = int.from_bytes(h.digest(),byteorder='big')

	bebe = bebe % q
	

	k = random.randrange(1, q - 2)
	r = pow(g, k, p) % q
	s = ( alpha * r - k * bebe ) % q

	return s,r


def SignVer(m, s, r, q, p, g, beta):

	h = SHA3_256.new()
	h.update(m)

	bebe = int.from_bytes(h.digest(),byteorder='big')

	bebe = bebe % q
	
	v = Crypto.Util.number.inverse(bebe, q)

	z1 = (s * v) % q

	z2 = (v * r) % q

	

	u = ((pow(g,-z1,p) * pow(beta,z2,p)) % p) % q

	if u == r:
		return 0
	else:
		return -1
