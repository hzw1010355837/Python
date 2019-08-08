

l = [54, 26, 17, 31, 44, 55, 20]

def choose_sort(alist):
    n = len(alist)

    # 对第i个元素进行选择
    for i in range(n-1):
        # i,就是选择的对象

        # 对第i个元素进行选择，首先假设第i个元素就是此次选择中最小的元素
        min_index = i

        # 每次选择的时候第i个元素分别和第j个元素进行比较
        for j in range(i+1, n):
            # i: 前置比较对象
            # j： 后置比较对象
            # alist[i]   alist[j]
            # if alist[i] > alist[j]:
                # 大的放后，小的放前： 升序 --- 反之降序
                # alist[i], alist[j] = alist[j], alist[i]

            # 假设的min_index和j进行比较，如果min_index比j大，重新记录min_index
            if alist[min_index] > alist[j]:
                min_index = j

        # min_index记录的就是当次选择中最小的那个元素的下标
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index],alist[i]

choose_sort(l)
print(l)