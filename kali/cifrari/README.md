Codice di esempio per crittografia classica
===========================================

Implementazione (assolutamente ingenua) degli algoritmi di base per l'applicazione dei cifrari a flusso e a blocchi. Commenti disponibili nel codice.

Cifrari a flusso (_stream cyphers_)
-----------------------------------

Altrimenti detti OTP (_one-time pad_).

  * `otp.py`: cifrario a flusso che utilizza un file "chiave" contenente byte casuali;
  * `otp2.py`: cifrario a flusso che utilizza una chiave di tipo stringa come seme per inizializzare un generatore di byte casuali.

Cifrari a blocchi (_block cyphers_)
-----------------------------------

  * `ecb.py`: cifrario a blocchi (blocchi da un byte, cifratura data dallo XOR con una chiave fissa) in modalità ECB;
  * `cbc_encode.py`, `cbc_decode.py`: cifrario a blocchi (blocchi da un byte, cifratura data dallo XOR con una chiave fissa) in modalità CBC.
