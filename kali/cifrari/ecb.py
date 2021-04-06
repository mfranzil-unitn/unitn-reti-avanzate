#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# ecb.py
#
# Programma minimale per l'applicazione di un cifrario
# a blocchi su un messaggio, in modalità ECB (Electronic Codebook)
# in cui ogni blocco viene cifrato separatamente.
#
# Nel nostro caso, un blocco corrisponde a un byte, e l'algoritmo
# di cifratura consiste nell'OR esclusivo con una chiave fissa a 8 bit.
#
# Istruzioni:
#
# - creare un file, messaggio.txt, contenente il messaggio in chiaro
# - eseguire il comando
#     python ecb.py messaggio.txt 154 codice.bin
# - verificare che il file creato, codice.bin, non è leggibile; però
#   a lettera uguale corrisponde codice uguale
# - decifrare il codice riapplicando la procedura:
#     python ecb.py codice.bin 154 decodifica.txt
# - verificare che decodifica.txt e messaggio.txt sono uguali.
#
# Osservare che le operazioni di codifica e decodifica sono identiche.
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

# sys.argv[1] è il nome del file contenente il messaggio
f = open(sys.argv[1], 'r')
m = f.read()
f.close()

# La chiave è un numero intero (sys.argv[n] è una stringa, assumiamo che
# codifichi un intero adatto)
k = int(sys.argv[2])

#########################
#
# Creazione del codice
#

c = ''
for i in range(len(m)):
	v = ord(m[i])
	# Il codice di ogni carattere è posto in OR esclusivo con la stessa chiave.
	c = c + chr(v^k)

##########################
#
# Scrittura del codice
#

f = open(sys.argv[3], 'w') # codice
f.write(c)
f.close()
