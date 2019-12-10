from Crypto.Hash import SHA3_256


def CheckPow(p, q, g, nonce_lenght, TxCnt, file):

	f = open(file,"r")
	block = f.readlines()
	f.close()

	storeHash = []

	

	for i in range(0, TxCnt):
		
		tx = "".join(block[i*7: i*7+5]).rstrip()

		print(tx)
		
		h = SHA3_256.new()
		
		h.update(tx.encode("UTF-8"))
	
		storeHash.append(h.digest())



	#Generate Root Hash
	while len(storeHash) > 1:

		
		j = 0

		for i in range(0, len(storeHash) - 1): 
			
			concat = storeHash[i] + storeHash[i+1]

			h2 = SHA3_256.new()
			h2.update(concat)

			storeHash[j] = h2.digest()
			

			i += 2
			j += 1

		lastDelete = i - j;

		del storeHash[-lastDelete:];


	h3 = SHA3_256.new()

	nonce = 277157211575692414559330522236021589363

	digest = storeHash[0] + ((str(nonce)+'\n')).encode("UTF-8")

	h3.update(digest)

	return h3.hexdigest()












            

