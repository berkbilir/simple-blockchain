from Crypto.Hash import SHA3_256

def merkleRoot(storeHash):

	result = []

	temp = []

	n = 2
	storeHash = [storeHash[k:k+n] for k in range(0, len(storeHash), n)]

	j = 0

	for i in storeHash:

		temp = storeHash[i]

		storeHash[i] = temp[j] + temp[j+1]

		h2 = SHA3_256.new()
		h2.update(storeHash[i].encode("UTF-8"))

		result.append(h2)

		temp = []

		























def CheckPow(p, q, g, nonce_lenght, TxCnt, file):

	f = open(file,"r")
	block = f.readlines()
	f.close()

	storeHash = []

	

	for i in range(0, TxCnt):
		
		tx = "".join(block[i*7: i*7+5])
		
		h = SHA3_256.new()
		
		h.update(tx.encode("UTF-8"))
	
		storeHash.append(h.hexdigest())

	merkleRoot(storeHash)

	#Generate Root Hash
	while len(storeHash) > 1:


		j = 0

		for i in range(0, len(storeHash) - 1): 
			
			concat = storeHash[i] + storeHash[i+1]

			h2 = SHA3_256.new()
			h2.update(concat.encode("UTF-8"))

			storeHash[j] = h2.hexdigest()
			

			i += 2
			j += 1

		lastDelete = i - j;

		del storeHash[-lastDelete:];

	h3 = SHA3_256.new()

	h3.update((storeHash[0] + "277157211575692414559330522236021589363").encode("UTF-8"))

	

	return h3.hexdigest()











            

