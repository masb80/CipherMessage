#!/usr/bin/python3.5
# encoding: utf-8

'''
@author:        Samad Bhuiyan
@Descriptions   Write a program that allows a user to encrypt and decrypt a message.

'''

import base64;
from Crypto.Cipher import AES;
from Crypto import Random;

KEY = "bl1ea2bb8288358aa4078011e8724697"
class CipherText():
    def __init__(self):
        self.key = KEY

    def encrypt(self, message):
        RIV = Random.new().read(AES.block_size)
        cipr = AES.new(self.key, AES.MODE_CFB, RIV)
        cipmessage = cipr.encrypt(message)
        encryptedmessage = str(base64.b64encode(RIV + cipmessage), 'utf8')     
        return  encryptedmessage

    def decrypt(self, encryptedmessage):
        encmsg = base64.b64decode(encryptedmessage)
        cipr = AES.new(self.key, AES.MODE_CFB, encmsg[:16])
        decryptedmessage = str(cipr.decrypt(encmsg[16:]), 'utf8') 
        return  decryptedmessage    

cip = CipherText()
try:
    inmessage = input('Please enter a message: ')
    print("The initial message is:  " + str(inmessage))
    enmessage = cip.encrypt(inmessage)
    print("The encrypted message is:  " + enmessage)
    decmessage = cip.decrypt(enmessage)
    print("The decrypted message is:  " + decmessage)
    
except EOFError as e: 
    print(e)  