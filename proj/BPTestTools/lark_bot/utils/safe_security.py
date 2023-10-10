# -*- coding: utf-8 -*-
"""
@Author: shining
@File: safe_security.py
@Date: 2022/8/11 11:12 下午
@Version: python 3.9
@Describe:
"""

import binascii
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5


class RsaCrypto():
    '''RSA 加解密'''

    def create_rsa_key(self):
        '''生成RSA秘钥对'''
        try:
            key = RSA.generate(2048)
            encrypted_key = key.exportKey(pkcs=8)

            public_key = key.publickey().exportKey().decode('utf-8')
            private_key = encrypted_key.decode('utf-8')

            return {'state': 1, 'message': {'public_key': public_key, 'private_key': private_key}}
        except Exception as err:
            return {'state': 0, 'message': str(err)}

    def encrypt(self, public_key, plaintext):
        '''加密方法'''
        try:
            recipient_key = RSA.import_key(public_key)
            cipher_rsa = PKCS1_v1_5.new(recipient_key)

            en_data = cipher_rsa.encrypt(plaintext.encode('utf-8'))
            hex_data = binascii.hexlify(en_data).decode('utf-8')

            return {'state': 1, 'message': hex_data}
        except Exception as err:
            return {'state': 0, 'message': str(err)}

    def decrypt(self, private_key, hex_data):
        '''解密方法'''
        try:
            private_key = RSA.import_key(private_key)
            cipher_rsa = PKCS1_v1_5.new(private_key)

            en_data = binascii.unhexlify(hex_data.encode('utf-8'))
            data = cipher_rsa.decrypt(en_data, None).decode('utf-8')

            return {'state': 1, 'message': data}
        except Exception as err:
            return {'state': 0, 'message': str(err)}


if __name__ == '__main__':
    print(RsaCrypto().create_rsa_key())
