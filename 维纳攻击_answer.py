import gmpy2
import libnum


def continuedFra(x, y):
    """计算连分数
    :param x: 分子
    :param y: 分母
    :return: 连分数列表
    """
    cf = []
    while y:
        cf.append(x // y)
        x, y = y, x % y
    return cf


def gradualFra(cf):
    """计算传入列表最后的渐进分数
    :param cf: 连分数列表
    :return: 该列表最后的渐近分数
    """
    numerator = 0
    denominator = 1
    for x in cf[::-1]:
        # 这里的渐进分数分子分母要分开
        numerator, denominator = denominator, x * denominator + numerator
    return numerator, denominator


def solve_pq(a, b, c):
    """使用韦达定理解出pq，x^2−(p+q)∗x+pq=0
    :param a:x^2的系数
    :param b:x的系数
    :param c:pq
    :return:p，q
    """
    par = gmpy2.isqrt(b * b - 4 * a * c)
    return (-b + par) // (2 * a), (-b - par) // (2 * a)


def getGradualFra(cf):
    """计算列表所有的渐近分数
    :param cf: 连分数列表
    :return: 该列表所有的渐近分数
    """
    gf = []
    for i in range(1, len(cf) + 1):
        gf.append(gradualFra(cf[:i]))
    return gf


def wienerAttack(e, n):
    """
    :param e:
    :param n:
    :return: 私钥d
    """
    cf = continuedFra(e, n)
    gf = getGradualFra(cf)
    for d, k in gf:
        if k == 0: continue
        if (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) // k
        p, q = solve_pq(1, n - phi + 1, n)
        if p * q == n:
            return d


n = 92271933885951017762581233309462527201517070039879532286159565838279004832845676335938665446902205232511332717613782699938868519349529541840054057788855500583484961363840775975590633423331145436923764705739151938836391016840976777016000483799864442516364604629706726137229542895540322473522942569065524718311
e = 58555611954114310618893162272588176201690193603964290327199059677590178868272525858842877638014996941248064153343429462984439330175442341662258832962376353060317706874486213106603426623488162727972095506094650079162437187599946189092969307682615885367569409671717672750817095364950370842991221989860603476649
c = 34615810713293500348475388029135854692898670706574827158433358288328945523283705878691811817046939492469866861694140834053649838799883474373353439233521438825602695778418080180674369317467216176042244138138072556059085682960919544395294984426093409949643782285659346133674797006979725465930419719293694928447

d = wienerAttack(e, n)
m = pow(c, d, n)
print(libnum.n2s(m).decode())
