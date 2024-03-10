import libnum
import gmpy2

p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)

N = p * q

phi_N = (p - 1) * (q - 1)

e = 65537

d = gmpy2.invert(e, phi_N)

flag = "flag{Hello_RSA}"

m = libnum.s2n(flag)

c = pow(m, e, N)

print("p=", p)
print("q=", q)
print("n=", N)
print("e=", e)
print("c=", c)
print("d=", d)
