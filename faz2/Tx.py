import random
import DS

#Berk Bilir 23621
#Doğukan Köksal 24305

def gen_random_tx(q, p, g):

	serialNumber = random.getrandbits(128)
	amount = random.randint(1, 1000000)
	
	Payer_Alpha, PayerPK_Beta = DS.KeyGen(q,p,g)
	Payee_Alpha, PayeePK_Beta = DS.KeyGen(q,p,g)

	m = "**** Bitcoin transaction ****\n" + "Serial number: " + str(serialNumber) + "\n" "Payer public key (beta): " + str(PayerPK_Beta) + "\n" "Payee public key (beta): " + str(PayeePK_Beta) + "\n" "Amount: " + str(amount) + "\n"

	signiture_s, signiture_r = DS.SignGen(m.encode('UTF-8'),q,p,g,Payer_Alpha)

	tx = "**** Bitcoin transaction ****\n" + "Serial number: " + str(serialNumber) + "\n" "Payer public key (beta): " + str(PayerPK_Beta) + "\n" "Payee public key (beta): " + str(PayeePK_Beta) + "\n" "Amount: " + str(amount) + "\n" "Signiture (s): " + str(signiture_s) + "\n" "Signiture (r): " + str(signiture_r) + "\n" 

	return tx


def gen_random_txblock(q, p, g, TxCnt, file):

	f = open(file,"w")
	
	i = 0

	while i != TxCnt:
		
		serialNumber = random.getrandbits(128)
		amount = random.randint(1, 1000000)
		
		Payer_Alpha, PayerPK_Beta = DS.KeyGen(q,p,g)
		Payee_Alpha, PayeePK_Beta = DS.KeyGen(q,p,g)

		m = "**** Bitcoin transaction ****\n" + "Serial number: " + str(serialNumber) + "\n" "Payer public key (beta): " + str(PayerPK_Beta) + "\n" "Payee public key (beta): " + str(PayeePK_Beta) + "\n" "Amount: " + str(amount) + "\n"

		signiture_s, signiture_r = DS.SignGen(m.encode('UTF-8'),q,p,g,Payer_Alpha)

		tx = "**** Bitcoin transaction ****\n" + "Serial number: " + str(serialNumber) + "\n" "Payer public key (beta): " + str(PayerPK_Beta) + "\n" "Payee public key (beta): " + str(PayeePK_Beta) + "\n" "Amount: " + str(amount) + "\n" "Signiture (s): " + str(signiture_s) + "\n" "Signiture (r): " + str(signiture_r) + "\n" 

		f.write(str(tx))

		i = i + 1

	f.close()
