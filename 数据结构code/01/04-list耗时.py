




# 尾部追加:
# l.append(value)
# 头部插入:
# l.insert(0,  value)
#
# 列表相加:
# [ ] + [xx]
#
# 列表生成式:
# [x for x in range(100)]
#
# 通过可迭代对象实例化一个列表对象:
# list(range(100))


def test1():
    # 尾部追加
    l = []
    for i in range(1000):
        l.append(i)

def test2():
    # 头部插入
    l = []
    for i in range(1000):
        l.insert(0, i)


def test3():
    # 列表相加
    l = []
    for i in range(1000):
        l += [i]


def test4():
    # 列表生成式
    l = [x for x in range(1000)]

def test5():
    # 通过可迭代对象实例化一个列表对象
    l = list(range(1000))

from timeit import Timer


t1 = Timer(stmt="test1()", setup="from %s import test1" % __name__)
print("尾部追加:", t1.timeit(number=10000))

t2 = Timer(stmt="test2()", setup="from %s import test2" % __name__)
print("头部插入:", t2.timeit(number=10000))

t3 = Timer(stmt="test3()", setup="from %s import test3" % __name__)
print("列表相加:", t3.timeit(number=10000))

t4 = Timer(stmt="test4()", setup="from %s import test4" % __name__)
print("列表生成式:", t4.timeit(number=10000))

t5 = Timer(stmt="test5()", setup="from %s import test5" % __name__)
print("可迭代对象实例化:", t5.timeit(number=10000))


# 尾部追加: 1.6018411239929264
# 头部插入: 5.361222387000453

# 列表相加: 2.2896942169900285
# 列表生成式: 0.5911178270034725
# 可迭代对象实例化: 0.21950286100036465