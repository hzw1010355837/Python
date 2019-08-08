


l = [17, 20, 26,       31,         44, 54, 55]



def binary_search(alist, data):

    start = 0
    end = len(alist) - 1


    while start <= end:
        # if start > end:
        #     break

        # 判断中间值
        mid_index = (start + end) // 2
        if alist[mid_index] == data:
            return True

        # start右移确定右表 --> 当中间值比data小的时候
        if alist[mid_index] < data:
            start = mid_index + 1

        # end左移确定左表 --> 中间值比data大
        else:
            end = mid_index - 1

        # start和end确定了一张新表

    return False


print(binary_search(l, 154))