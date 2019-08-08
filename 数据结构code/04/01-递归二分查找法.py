


l = [17, 20, 26,       31,         44, 54, 55]


def binary_search(alist, data):

    # 如果递归下来的是一张空表，就说明猜完了
    if len(alist) == 0:
        return False

    n = len(alist)


    # 确定一个中间下标
    mid_index = n//2

    # 判断所查找的数是不是中间数
    if alist[mid_index] == data:
        return True

    # 如果不是需要确定在左表中还是在有表中
    # 中间值比data大在左表中，否则在右表中 --- 升序
    # 在左表或者有表中在猜中间值
    if alist[mid_index] > data:
        left_list = alist[:mid_index] # 生成一个新的列表
        # 递归查找左表
        return binary_search(left_list, data)
    else:
        right_list = alist[mid_index+1:]
        # 递归查找右表
        return binary_search(right_list, data)



print(binary_search(l, 54))


