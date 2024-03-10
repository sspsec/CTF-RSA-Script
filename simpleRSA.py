import libnum
import gmpy2

p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
N = p * q
e = 65537
phi_N = (p - 1) * (q - 1)  # N的欧拉函数
d = gmpy2.invert(e, phi_N)  # d是e在phi_N下的乘法逆元

flag = "flag{aec16fe46c12fa6d223b410dddf3f7c5}"

m = libnum.s2n(flag)
c = pow(m, e, N)

print("n=", N)
print("d=", d)
print("e=", e)
print("c=", c)
