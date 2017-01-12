from Crypto.PublicKey import RSA


def create_keys():
    key = RSA.generate(2048)
    encrypted_key = key.exportKey()
    return encrypted_key, key.publickey().exportKey('OpenSSH')
