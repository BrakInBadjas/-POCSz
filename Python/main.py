import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5

import os
import encrypt

if not os.path.exists('privateKey.pem'):
    encrypt.newKey()
 
# Use a larger key length in practice...
KEY_LENGTH = 2048  # Key size (in bits)
random_gen = Random.new().read
 
# Generate RSA private/public key pairs for both parties...
keypair_snowden = encrypt.loadKeyFromFile('privateKey.pem')
keypair_pytn    = encrypt.loadKeyFromFile('privateKey.pem')
 
# Public key export for exchange between parties...
pubkey_snowden  = keypair_snowden.publickey()
pubkey_pytn     = keypair_pytn.publickey()
 
# Plain text messages...
message_to_snowden  = b'You are a patriot!'
message_to_pytn     = b"Russia is really nice this time of year... Use encryption and make the NSA CPUs churn and burn!"
 
# Encrypt messages using the other party's public key...
encrypted_for_snowden   = pubkey_snowden.encrypt(message_to_snowden, 32)    #from PyTN
encrypted_for_pytn      = pubkey_pytn.encrypt(message_to_pytn, 32)          #from Snowden
 
# Decrypt messages using own private keys...
decrypted_snowden   = keypair_snowden.decrypt(encrypted_for_snowden)
decrypted_pytn      = keypair_pytn.decrypt(encrypted_for_pytn)
 
print("Edward Snowden received from PyTn:")
print(encrypted_for_snowden)
print(decrypted_snowden.decode("utf-8"))
print("")

print("PyTN received from Edward Snowden:")
print(encrypted_for_pytn)
print(decrypted_pytn.decode("utf-8"))
