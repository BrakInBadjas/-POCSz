import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import db

#Encrypt message with public key
def encrypt(public_key, msg):
	encrypted = public_key.encrypt(msg, 'x')[0]
	return encrypted

#Decrypt message with private key
def decrypt(private_key, msg):
	decrypted = private_key.decrypt(msg)
	return decrypted
	
#Load a key from a file
def loadKeyFromFile(file_name):
	with open(file_name + '.txt', 'r') as content_file:
		content = content_file.read()
	return RSA.importKey(content)
	
#Load a public key from the database
def loadKeyFromDatabase(door_id):
	key = db.getDoorPublicKey(door_id)
	return RSA.importKey(key)