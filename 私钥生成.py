from Crypto.PublicKey import RSA
import gmpy2
import libnum

p = libnum.generate_prime(1024)
q = gmpy2.next_prime(p)
N = p * q
e = 65537
phi_N = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi_N)

rsa_c = (int(N), int(e), int(d))

keypair = RSA.construct(rsa_c)

with open("privatekey.pem", "wb") as f:
    f.write(keypair.exportKey())
