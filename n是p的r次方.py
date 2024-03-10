import libnum

# 生成随机素数
p = libnum.generate_prime(256)
e = 65537
m = "flag{de8c3ea714f7f780185924d473997bcb}"
# 字符串转数字
m = libnum.s2n(m)
n = p ** 4
phi_n = p ** 4 - p ** 3
# 求逆元
d = libnum.invmod(e, phi_n)
c = pow(m, e, n)

print("n=", n)
print("e=", e)
print("c=", c)
