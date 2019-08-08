

l = [54, 26, 17, 31, 44, 55, 20]




def insert_sort(alist):
    n = len(alist)

    # 抽牌的下标取值范围i
    for i in range(1, n): # O(n)
        # 1,2,3...n-1 -- 右手牌
        # 抽到第i张牌
        # 第j和j-1张牌分别进行比较交换
        for j in range(i, 0, -1): # O(n)
            if alist[j] < alist[j-1]:
                # j小于j-1交换，表示小的放前是升序， 反之降序
                alist[j],alist[j-1] = alist[j-1],alist[j]
            else:
                break



insert_sort(l)
print(l)