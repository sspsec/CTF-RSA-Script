# coding:utf-8
import random
import hashlib
import string
import libnum


def put_flag():
    # 字符串列表
    a = string.printable
    flag = ""
    for i in range(10):
        flag += a[random.randint(0, 99)]
    flag = r"flag{%s}" % (hashlib.md5(flag.encode()).hexdigest())
    print(flag)
    return flag


# 生成素数
p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
e = 65537
n = p * q
phi_n = (p - 1) * (q - 1)
d = libnum.invmod(e, phi_n)
dp = d % (p - 1)
m = put_flag()
m = libnum.s2n(m)
n = p * q
c = pow(m, e, n)

print("n=", n)
print("e=", e)
print("dp=", dp)
print("c=", c)
