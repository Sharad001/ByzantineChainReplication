import nacl.encoding
import nacl.signing
import nacl.hash
import pickle
from nacl.bindings.utils import sodium_memcmp
from enum import Enum


class State(Enum):
	PENDING = 0
	ACTIVE = 1
	IMMUTABLE = 2

class Utils:
	def __init__(self):
		self.HASHER = nacl.hash.sha256
	def getSignedStatement(self, signing_key, statement):
		return nacl.signing.SigningKey(signing_key, encoder=nacl.encoding.HexEncoder).sign(statement.encode())
	def getHash(self, statement):
		return self.HASHER(statement.encode(), encoder=nacl.encoding.HexEncoder)

	def verifySignature(self, statement, public_key):
		verify_key = nacl.signing.VerifyKey(public_key, encoder=nacl.encoding.HexEncoder)
		return verify_key.verify(statement)

	def verifyHash(self, statement, digest):
		statementdigest = self.getHash(statement)
		if sodium_memcmp(statementdigest, digest):
			return True
		else:
		 	return False

	def verifyTwoHash(self, hash1, hash2):
		if sodium_memcmp(hash1, hash2):
			return True
		else:
		 	return False
	def getSignedKey(self):
    		signing_key = nacl.signing.SigningKey.generate()
    		verify_key = signing_key.verify_key
    		verify_key_hex = verify_key.encode(encoder=nacl.encoding.HexEncoder)
    		sign_key_hex = signing_key.encode(encoder=nacl.encoding.HexEncoder)
    		return (sign_key_hex,verify_key_hex)

	def getInvalidSignedStatement(self, signed_statement):
		signedlist = list(signed_statement)
		signedlist[0] = (signedlist[0] + 1) % 256
		newsigned = bytes(signedlist)
		invalid_signed = nacl.signing.SignedMessage._from_parts(signed_statement._signature, signed_statement._message, newsigned)
		return invalid_signed
