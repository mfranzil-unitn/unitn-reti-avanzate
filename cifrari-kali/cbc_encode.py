#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# cbc_encode.py
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
# - creare un file, messaggio.txt, contenente il messaggio in chiaro
# - eseguire il comando
#     python cbc_encode.py messaggio.txt 154 codice.bin
# - verificare che il file creato, codice.bin, non è leggibile, e che lettere
#   uguali nel messaggio vengono comunque codificate diversamente
# - utilizzare cbc_decode.py per la decodifica
#
# Osservare che in CBC le operazioni di codifica e decodifica non sono
# più simmetriche.
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
m = f.read()
f.close()

k = int(sys.argv[2])

#########################
#
# Creazione del codice
#

c = ''
# c0 è il codice del blocco precedente
c0 = 0
for i in range(len(m)):
	# Prima della codifica, mettiamo il blocco attuale in OR esclusivo con
	# il codice del blocco precedente
	v = ord(m[i]) ^ c0
	c0 = v ^ k
	c = c + chr(c0)

##########################
#
# Scrittura del codice
#

f = open(sys.argv[3], 'w')
f.write(c)
f.close()
