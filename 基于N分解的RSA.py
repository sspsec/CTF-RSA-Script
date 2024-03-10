import libnum
import gmpy2

flag = "flag{d07a2a42ffc72496970337e14c66c810}"

p = libnum.generate_prime(1024)
q = gmpy2.next_prime(p)

N = p * q
e = 65537
m = libnum.s2n(flag)
c = pow(m, e, N)

print("n=", N)
print("e=", e)
print("c=", c)
