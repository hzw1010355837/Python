

l = [54, 26, 17,  31, 44, 55, 20]



def quick_sort(alist, start, end):
    if start >= end:
        return

    low = start
    high = end

    mid = alist[low]

    while low < high: # low和high相遇的时候退出循环
        # if low >= high:
        #     break

        # 高位high指向的数大于mid的时候high左移
        while alist[high] >= mid and low < high:
            high -= 1
        alist[low] = alist[high]

        # 地位low指向的数小于mid的时候low右移
        while alist[low] < mid and low < high:
            low += 1
        alist[high] = alist[low]

    # low == high
    alist[low] = mid

    # 左表:   [start, low-1]
    quick_sort(alist, start, low-1)

    # 右表:   [high+1, end]
    quick_sort(alist, high+1, end)


quick_sort(l, 0, 6)
print(l)