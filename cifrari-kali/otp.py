#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# otp.py
#
# Programma minimale per la codifica e la decodifica
# di un messaggio con una chiave OTP (one-time pad).
#
# Istruzioni:
#
# - costruire un file chiave lungo almeno quanto il
#   messaggio da spedire e contenente bit casuali. Ad esempio,
#   in un sistema Unix è sufficiente copiare un numero adeguato (1MB) di byte
#   da /dev/urandom in un file (chiave.bin):
#     dd if=/dev/urandom of=chiave.bin bs=1M count=1
# - creare un file, messaggio.txt, contenente il messaggio in chiaro
# - eseguire il comando
#     python otp.py messaggio.txt chiave.bin codice.bin
# - verificare che il file creato, codice.bin, non è leggibile
# - decifrare il codice riapplicando la procedura:
#     python otp.py codice.bin chiave.bin decodifica.txt
# - verificare che decodifica.txt e messaggio.txt sono uguali.
#
# Osservare che le operazioni di codifica e decodifica sono identiche.
#
# Attenzione: il codice ha scopo puramente dimostrativo.

###################
#
# Importazione dei pacchetti
#

# Accedere ai parametri della linea di comando
import sys

######################
#
# Lettura dei dati di input (messaggio e chiave)
#

# sys.argv[1] è il nome del file contenente il messaggio
f = open(sys.argv[1], 'rb')
# Leggiamo tutto il messaggio in memoria nella stringa m
m = f.read()
# chiudiamo il file
f.close()

# Idem per la chiave
f = open(sys.argv[2], 'rb')
k = f.read()
f.close()

#########################
#
# Creazione del codice
#

# c è la variabile nella quale accumuliamo i caratteri del codice
c = ''
# Iteriamo su tutti i caratteri (byte) del messaggio
for i in range(len(m)):
	# Codice numerico (ASCII) dell'i-esimo carattere del messaggio
	v = ord(m[i])
	# Codice numerico corrispondente all'i-esimo byte della chiave
	w = ord(k[i])
	# Calcoliamo l'or esclusivo (operatore "^") fra un byte del messaggio e un byte della chiave
	# Poi interpretiamo il byte risultante come carattere per appenderlo alla stringa c
	c = c + chr(v^w)

##########################
#
# Scrittura del codice
#

# Scriviamo la stinga c nel file il cui nome si trova nel terzo argomento della riga di comando
f = open(sys.argv[3], 'wb')
f.write(c)
f.close()
