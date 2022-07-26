# from aiogram import types
# from aiogram.dispatcher.filters import Command
import tronpy
from ecdsa import SigningKey
from tronpy import Tron, keys
from tronpy.keys import PrivateKey


# Library hash
# import bcrypt

# from loader import dp

# connect to the Tron blockchain
from utils.encryption import decrypt_xor

# client = Tron()  # Maintest
client = Tron(network="nile")  # Test
print('Подключение к блокчейну')


# chech whether the recipient's wallet address is a valid Tron address or not
def is_valid(address):
    is_address = client.is_address(str(address))
    return is_address


# create a Tron wallet and print out the wallet address & private key
def create_wallet():
    wallet = client.generate_address()
    if is_valid(wallet['base58check_address']):
        # user_wallet = "Wallet address:  %s" % wallet['base58check_address']
        # user_private_key = "Private Key:  %s" % wallet['private_key']
        user_wallet = wallet['base58check_address']
        user_private_key = wallet['private_key']
        return user_wallet, user_private_key
    else:
        return


# balance
def account_balance(address):
    balance = str(client.get_account_balance(str(address)))
    return balance


# Take address from private key
def take_address(private_key):
    try:
        address = client.generate_address(PrivateKey.fromhex(private_key))['base58check_address']
        if is_valid(address):
            return address
        else:
            return False
    except Exception:
        return False

# address = client.generate_address(PrivateKey.fromhex('adaf54b73c12b905867fd294310ec04cffa640a139dabd6797c2136206cb3541'))
# print(address['base58check_address'])
# withdraw


# integers representing half & one Tron
HALF_TRON = 500000
ONE_TRON = 1000000


# your wallet information
# WALLET_ADDRESS = "YOUR WALLET ADDRESS"
# PRIVATE_KEY = "YOUR WALLET PRIVATE KEY"


# def test():
#     priv_key = PrivateKey(bytes.fromhex('7c2dddf3b2f3c36c5e1ea151981355529cd257731a0223f0a85dbe71d03b4df7'))
#     return priv_key
#
#
# print(test())


# send some 'amount' of Tron to the 'wallet' address
def send_tron(user_wallet, wallet, amount, private_key, password):
    try:
        if password is None:
            priv_key = PrivateKey(bytes.fromhex(private_key[3:len(private_key) - 3]))
        else:
            priv_key = PrivateKey(bytes.fromhex(decrypt_xor(private_key[3:len(private_key) - 3], password)))
        # create transaction and broadcast it
        txn = (
            client.trx.transfer(user_wallet, str(wallet), int(amount))
            .memo("Transaction Description")
            .build()
            # .inspect()
            .sign(priv_key)
            .broadcast()
        )
        # wait until the transaction is sent through and then return the details
        print(type(amount))
        import sys
        print(sys.getsizeof(txn))
        print(sys.getsizeof(txn.txid))
        if amount is not 0:
            w = txn.wait(timeout=30, interval=1.7, solid=False)
            print(w)
            print(sys.getsizeof(w))
            return w
        else:
            return txn.wait()

    # return the exception
    except Exception as ex:
        # ('Account resource insufficient error.', 'BANDWITH_ERROR')
        print('send_tron: ', ex.args)
        print('send_tron: ', ex.args[0] == 'non-hexadecimal number found in fromhex() arg at position 0')
        return ex


def check_fee(user, wallet, amount):
    import sys
    try:
        txn = (
            client.trx.transfer(user.wallet, str(wallet), int(amount))
            .memo("test memo")
            .build()
            # .inspect()
            # .sign(priv_key)
        )
        size = sys.getsizeof(client.get_sign_weight(txn)['transaction']['transaction'][
                                 'raw_data_hex']) - 41
        return size

    # return the exception
    except Exception as ex:
        print('Сheck fee ERR: ', ex.args)
        return ex


# print('Check fee: ', check_fee('TQyEcdA6kKP3XkwsMQmyo5EnnRzehmgTtc', 'TMWXhuxiT1KczhBxCseCDDsrhmpYGUcoA9', '1000000000'))

def resource_tron(user_wallet):
    try:
        resource = client.get_account_resource(user_wallet)
        return resource

    # return the exception
    except Exception as ex:
        return ex


def address_check_func(user_wallet):
    try:
        address = client.is_address(user_wallet)
        return address
    # return the exception
    except Exception as ex:
        return ex


# def privat_check_func(private_key):
#     try:
#         # cdfdad = client.get_sign_weight()
#         answer = PrivateKey(bytes.fromhex(private_key))
#         return answer
#     # return the exception
#     except Exception as ex:
#         return ex


# print('Проверка функции', privat_check_func('b99656d515db429a4c32bb5d9dc3a5de2ff5ebf2ca480ff4209f74b3a1356583'))


# ______TRANSFER USDT
def usdt_transfer(self, to, amount, memo=''):
    # contract = client.get_contract('TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t')  # MainNet
    contract = client.get_contract('TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf')  # TestNet
    txn = (
        contract.functions.transfer.with_transfer(100_000_000)
        .call(to, 1_000)
        .with_owner(self.ADDRESS)  # address of the private key
        .fee_limit(5_000_000)
        .build()
        .sign(PrivateKey(bytes.fromhex(self.PRIV_KEY)))
    )
    txn.broadcast()
