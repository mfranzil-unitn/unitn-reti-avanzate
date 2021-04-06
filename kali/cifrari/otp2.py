#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# otp2.py
#
# Programma minimale per la codifica e la decodifica
# di un messaggio con una chiave OTP (one-time pad).
#
# A differenza di otp.py, utilizza una chiave breve come
# seme per un generatore pseudocasuale.
#
# Istruzioni:
#
# - creare un file, messaggio.txt, contenente il messaggio in chiaro
# - eseguire il comando
#     python otp2.py messaggio.txt "la mia chiave" codice.bin
# - verificare che il file creato, codice.bin, non è leggibile
# - decifrare il codice riapplicando la procedura:
#     python otp.py codice.bin "la mia chiave" decodifica.txt
# - verificare che decodifica.txt e messaggio.txt sono uguali.
#
# Osservare che le operazioni di codifica e decodifica sono identiche.
#
# Attenzione: il codice ha scopo puramente dimostrativo.
# In particolare, il generatore random utilizzato non è crittograficamente sicuro.

###################
#
# Importazione dei pacchetti
#

# Per l'accesso agli argomenti della riga di comando
import sys
# Generazione di numeri casuali
import random

######################
#
# Lettura dei dati di input (messaggio e chiave)
#

# sys.argv[1] è il nome del file contenente il messaggio
f = open(sys.argv[1], 'r')
m = f.read()
f.close()

# UTilizziamo il secondo argomento direttamente come seme per il generatore
k = sys.argv[2]
random.seed(k)

#########################
#
# Creazione del codice
#

c = ''
for i in range(len(m)):
	v = ord(m[i])
	# A differenza di otp.py, i byte della chiave vengono generati come
	# valori casuali a 8 bit (da 0 a 255)
	w = random.randint(0,255)
	c = c + chr(v^w)

##########################
#
# Scrittura del codice
#

f = open(sys.argv[3], 'w')
f.write(c)
f.close()





