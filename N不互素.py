import libnum

# 生成随机素数
p1 = libnum.generate_prime(1024)
p2 = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
e = 65537
m = "flag{c9d48baa792e91ce65d175bb586f8c24}"
# 字符串转数字
m = libnum.s2n(m)
n1 = p1 * q
n2 = p2 * q
# 求逆元
c1 = pow(m, e, n1)
c2 = pow(m, e, n2)

print("e=", e)
print("n1=", n1)
print("n2=", n2)
print("c1=", c1)
print("c2=", c2)
