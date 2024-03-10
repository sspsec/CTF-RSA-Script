import random
import hashlib
import string

a = string.printable

for i in range(10):
    flag = ""
    for j in range(10):
        flag += a[random.randint(0, 99)]
    flag = hashlib.md5(flag.encode()).hexdigest()

    print("flag{"+flag+"}")
