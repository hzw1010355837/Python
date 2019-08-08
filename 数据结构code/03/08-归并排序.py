

l = [54, 26, 17, 31, 44, 55, 20]



# 递归
def merge_sort(alist):

    if len(alist) == 1:
        return alist

    n = len(alist)

    left_list = merge_sort(alist[:n//2])
    right_list = merge_sort(alist[n//2:])


    return merge(left_list, right_list)


# 合并
def merge(left_list, right_list):
    left_index, right_index = 0, 0

    new_list = []

    while True: # O(n)
        if left_index > len(left_list) - 1 or right_index > len(right_list) - 1:
            break

        if left_list[left_index] < right_list[right_index]:
            new_list.append(left_list[left_index])
            left_index += 1
        else:
            new_list.append(right_list[right_index])
            right_index += 1

    new_list += left_list[left_index:]
    new_list += right_list[right_index:]

    return new_list


# l2 = [1,7,9,10,   2,5,7]

print(merge_sort(l))