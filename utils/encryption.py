from tronpy import exceptions
from tronpy.keys import PrivateKey

some_private_key = '6bd359d7634f8cbc07f80920b93f34515b32be149233b6ba03e116d73ff0e0ce'
password = 'nuOSv4V!LurN'
password2 = 'nuOSv4V!LurM'

# def crypto_xor(message: str, secret: str) -> str:
#     new_chars = list()
#     i = 0
#
#     for num_chr in (ord(c) for c in message):
#         num_chr ^= ord(secret[i])
#         new_chars.append(num_chr)
#
#         i += 1
#         if i >= len(secret):
#             i = 0
#
#     return ''.join(chr(c) for c in new_chars)


from itertools import cycle


def crypt(private_key, password):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(private_key, cycle(password)))


def encrypt_xor(message: str, secret: str) -> str:
    return crypt(message, secret).encode('utf-8').hex()


def decrypt_xor(message_hex: str, secret: str) -> str:
    message = bytes.fromhex(message_hex).decode('utf-8')
    return crypt(message, secret)


# encrypted = encrypt_xor(some_private_key, password)
# print(decrypt_xor('35907515704040a570007000751095051540104550f010a0107530a0051020706060451000553560203080100045305515601005606000557000255550754035052', '1337'))
# print(encrypted)
# print(some_private_key)
# with_salt = some_private_key[3:6] + encrypted + some_private_key[len(some_private_key) - 6:len(some_private_key) - 3]
# print('With salt: ' + with_salt)
# print('With salt: ' + with_salt[len(with_salt) - 3:])
# # print(some_private_key[5:2:-1] + some_private_key[len(some_private_key) - 3:len(some_private_key) - 6:-1])
# print(some_private_key[3:6] + some_private_key[len(some_private_key) - 6:len(some_private_key) - 3])
# print(encrypted)

#
# class DecryptXorPrivate:
#     def __init__(self, psw):
#         self.psw = psw
#
#     def func(self, priv):
#         return decrypt_xor(priv, self.psw)
#
#
# d = DecryptXorPrivate(password)  # d.func(user.private_key[3:len_private - 3])
# len_private = len(with_salt)
# len_1 = d.func(with_salt[3:len_private - 3])
# print(type(len_1), d.func(with_salt[3:len(with_salt) - 3]))
# print('Private key: ', d.func(with_salt[3:len_private - 3])[3:6] == with_salt[:3], d.func(with_salt[3:len_private - 3])[
#       len_1 - 6:
#       len(d.func(with_salt[3:len_private - 3])) - 3] == with_salt[len_private - 3:])

# print('Private key: ', decrypt_xor(with_salt[3:len(with_salt) - 3], password)[3:6] == with_salt[:3],
#       decrypt_xor(with_salt[3:len(with_salt) - 3], password)[
#       len(decrypt_xor(with_salt[3:len(with_salt) - 3], password)) - 6:
#       len(decrypt_xor(with_salt[3:len(with_salt) - 3], password)) - 3] == with_salt[len(with_salt) - 3:])
# 59167d37125030122e47147d0d467930435167442d44477f574d7e60430163137516167c5b427860475566137e46147e0f4d7a37145161102845412c5a112964

# print(decrypt_xor(encrypted, password))
# # 7c2dddf3b2f3c36c5e1ea151981355529cd257731a0223f0a85dbe71d03b4df7
#
# print(decrypt_xor(
#     "59167d37125030122e47147d0d467930435167442d44477f574d7e60430163137516167c5b427860475566137e46147e0f4d7a37145161102845412c5a112964",
#     password))
#
# h = '0a02d48b22081c9a4b7e61e9415940c0caee8a983052175472616e73616374696f6e204465736372697074696f6e5a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a15418d2f942be9ec9e56ad5e49a13cc3c85c6d821a8f121541055f5665db1d88d6fe052dd1a08fadee8afd3b3e1880c2d72f70e0f5ea8a9830'
#
#
# def test():
#     try:
#         priv_key = (bytes.fromhex(
#             '0a02d48b22081c9a4b7e61e9415940c0caee8a983052175472616e73616374696f6e204465736372697074696f6e5a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a15418d2f942be9ec9e56ad5e49a13cc3c85c6d821a8f121541055f5665db1d88d6fe052dd1a08fadee8afd3b3e1880c2d72f70e0f5ea8a9830'))
#         return priv_key
#     except ValueError:
#         return 'Не верный пароль'
#
#
# import sys
# # print(sys.getsizeof(f))
# # print('test: ', test())
#
#
# import os
#
# # f is a file-like object.
# f = {
#     "ret": [
#         {
#             "contractRet": "SUCCESS"
#         }
#     ],
#     "signature": [
#         "3cb56da695132675f1171cfb733cf0c83fb6319c13ea47389d38f0d939b6ffb01ce7ba412399424e830fc66c0416553f8a58ac2277f65b19045cd8b824fcd26701"
#     ],
#     "txID": "c0099e74027cf2c543a8e447ca5e27b75830c7ce97f5a52aad2d314b7c085f2f",
#     "raw_data": {
#         "data": "5472616e73616374696f6e204465736372697074696f6e",
#         "contract": [
#             {
#                 "parameter": {
#                     "value": {
#                         "amount": 100000000,
#                         "owner_address": "TNqjGwTVL7AxvUQhpkeyv3rbuR7GPqgtsg",
#                         "to_address": "TATcbBaYybAD9ubSbrfhw6qA7NtCVYQXDy"
#                     },
#                     "type_url": "type.googleapis.com/protocol.TransferContract"
#                 },
#                 "type": "TransferContract"
#             }
#         ],
#         "ref_block_bytes": "d48b",
#         "ref_block_hash": "1c9a4b7e61e94159",
#         "expiration": 1655732675904,
#         "timestamp": 1655732615904
#     },
#     "raw_data_hex": "0a02d48b22081c9a4b7e61e9415940c0caee8a983052175472616e73616374696f6e204465736372697074696f6e5a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a15418d2f942be9ec9e56ad5e49a13cc3c85c6d821a8f121541055f5665db1d88d6fe052dd1a08fadee8afd3b3e1880c2d72f70e0f5ea8a9830"
# }
# print(sys.getsizeof(f))
# print('test: ', test())
