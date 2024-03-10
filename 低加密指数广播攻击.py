import libnum


# 生成随机素数
def rsa_def(e, m):
    p = libnum.generate_prime(1024)
    q = libnum.generate_prime(1024)
    # 字符串转数字
    m = libnum.s2n(m)
    n = p * q
    c = pow(m, e, n)
    n_lt.append(n)
    c_lt.append(c)


n_lt = []
c_lt = []
e = 23
m = 'flag{2cb2eb4b2c7fdf4e94e10344be856446}'
for i in range(7):
    rsa_def(e, m)

print("e=", e)
print("n=", n_lt)
print("c=", c_lt)
