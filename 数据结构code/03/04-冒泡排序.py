

l = [54, 26, 17, 31, 44, 55, 20]

def pop_sort(alist):
    n = len(alist)

    # 需要进行冒泡的次数
    for i in range(n-1):
        # 0,1,2,...,n-2
        # 第i次冒泡
        # num记录本次冒泡交换的次数
        num = 0

        for j in range(n-1-i):
            # 进行比较： j和j+1比较，大的放后
            if alist[j] > alist[j+1]:
                alist[j], alist[j + 1] = alist[j+1],alist[j]
                num += 1


        if num == 0:
            # 说明本次冒泡没有发生交换，继而说明剩余未排序的元素本身就是有序的
            break

pop_sort(l)
print(l)