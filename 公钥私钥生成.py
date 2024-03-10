from Crypto.PublicKey import RSA
import gmpy2
import libnum

p = libnum.generate_prime(1024)
q = gmpy2.next_prime(p)
N = p * q
e = 65537
phi_N = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi_N)
flag = "flag{7e02dbd1a9c0aa4b159163331a0c2bef}"
m = libnum.s2n(flag)

c = pow(m, e, N)
c1 = libnum.n2s(int(c))
with open("flag.pem", "wb") as f:
    f.write(c1)

rsa_c = (int(N), int(e))  # 公钥生成
keypair = RSA.construct(rsa_c)
with open("publickey.pem", "wb") as f:
    f.write(keypair.exportKey())
#
# rsa_c = (int(N), int(e), int(d))  # 私钥生成
# keypair = RSA.construct(rsa_c)
# with open("privatekey.pem", "wb") as f:
#     f.write(keypair.exportKey())
