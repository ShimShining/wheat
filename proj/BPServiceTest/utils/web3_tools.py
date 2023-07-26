# -*- coding: utf-8 -*-
"""
@Author: xieguanglin
@File: web3_tools.py
@Date: 2022/12/28 11:20 上午
@Version: python 3.9
@Describe: web3 相关
No module named 'Crypto'的解决方案
使用pip命令安装以下依赖库，无视报错：
pip install pycryptodome
pip install crypto
pip install pycrypto
打开\Python\Python37\Lib\site-packages这个路径，找到crypto这个文件夹。
将crypto这个文件夹重命名为Crypto。
重新运行程序即可发现No module named 'Crypto'报错消失。

ImportError: cannot import name 'scrypt'
解决方案：https://github.com/ethereum/web3.py/issues/751
pip uninstall pycrypto
pip uninstall pycryptodome
pip install pycryptodome
"""
from eth_account import Account
from pprint import pprint

Account.enable_unaudited_hdwallet_features()


class Web3Tools:

    @staticmethod
    def create_new_ETH_wallet():

        account = Account.create_with_mnemonic()

        privateKey = account[0]._key_obj

        publicKey = privateKey.public_key

        address = publicKey.to_checksum_address()

        wallet = {
            "address": address,
            "privateKey": privateKey,
            "publicKey": publicKey,
            "mnemonic": account[1]
        }

        return wallet


if __name__ == '__main__':
     w = Web3Tools.create_new_ETH_wallet()
     pprint(w, width=100)

