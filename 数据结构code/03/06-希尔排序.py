

l = [54, 26, 17, 31,   44, 55, 20, 45]



def shell_sort(alist):
    n = len(alist)
    gap = n//2 # 4

    while gap > 0:
        # 4,2,1
        # if gap <= 0:
        #     break

        # 确定以一个分组的gap，分为gap个组
        # 每组插入排序

        # 抽牌的下标i取值范围
        for i in range(gap, n):
            # 抽到的第i张牌，插入到左手牌中

            for j in range(i, 0, 0-gap):
                # j和j-gap进行比较
                # 相邻比较，大的放后
                if alist[j] < alist[j-gap]:
                    alist[j],alist[j-gap] = alist[j-gap],alist[j]
                else:
                    break


        gap = gap//2


shell_sort(l)
print(l)

