from CryptoPals.Set2.AES_CBC_10 import CBC_encrypt
from CryptoPals.Set2.AES_ECB import pkcs7padding_validation
from Crypto.Cipher import AES
import random
import os

def func1(filepath = "17.txt"):
  def getRandomString(filepath) -> set[str]:
    random_strings = open(filepath).read().splitlines()
    return set(random_strings)
  rand_stringset = getRandomString(filepath)
  plaintext = random.choice(rand_stringset)
  global __AES_KEY
  __AES_KEY = os.urandom(16)
  IV = os.urandom(16)
  ciphertext = CBC_encrypt(plaintext, __AES_KEY, IV)
  return ciphertext, IV

def func2(ciphertext, enc_iv) -> bool:
  cipher = AES.new(__AES_KEY, AES.MODE_CBC, iv=enc_iv)
  plaintext = cipher.decrypt(ciphertext)
  try:
    pkcs7padding_validation(plaintext)
    return True
  except ValueError:
    return False

"""
attack plan:
  decribed in seperate text file.
"""

def decrypt_cipher_block(cipher_block, IV):
  pass
