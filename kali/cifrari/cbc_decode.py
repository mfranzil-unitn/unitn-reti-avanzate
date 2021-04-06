#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# cbc_decode.py
#
# Programma minimale per l'applicazione di un cifrario
# a blocchi su un messaggio, in modalità CBC (Chained Block Cypher)
# in cui ogni blocco viene messo in OR esclusivo con il codice
# del blocco precedente prima di essere cifrato.
#
# Nel nostro caso, un blocco corrisponde a un byte, e l'algoritmo
# di cifratura consiste nell'OR esclusivo con una chiave fissa a 8 bit.
#
# Istruzioni:
#
# - creare il file codice.bin come descritto in cbc_encode.py
# - decifrare il codice con il comando:
#     python cbc_decode.py codice.bin 154 decodifica.txt
# - verificare che decodifica.txt e messaggio.txt sono uguali.
#
# Attenzione: il codice ha scopo puramente dimostrativo.

###################
#
# Importazione dei pacchetti
#

import sys

######################
#
# Lettura dei dati di input (messaggio e chiave)
#

f = open(sys.argv[1], 'r')
c = f.read()
f.close()

k = int(sys.argv[2])

#########################
#
# Decifrazione del codice
#

m = ''
c0 = 0
for i in range(len(c)):
	v = ord(c[i])
	m = m + chr((v ^ k) ^ c0)
	c0 = v

##########################
#
# Scrittura del messaggio decifrato
#

f = open(sys.argv[3], 'w')
f.write(m)
f.close()





