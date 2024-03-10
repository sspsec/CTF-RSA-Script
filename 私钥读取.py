from Crypto.PublicKey import RSA
import libnum
import gmpy2

with open("privatekey.pem", "rb") as f:
    key = RSA.import_key(f.read())
    print("n=", key.n)
    print("d=", key.d)
    print("e=", key.e)
    print("p=", key.p)
    print("q=", key.q)
