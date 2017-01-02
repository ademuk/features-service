from Crypto.PublicKey import RSA


def create_keys():
    key = RSA.generate(2048)
    encrypted_key = key.exportKey(pkcs=8,
                                  protection="scryptAndAES128-CBC")
    return (encrypted_key, key.publickey().exportKey())