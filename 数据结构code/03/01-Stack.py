





class Stack(object):
    def __init__(self):
        self.__items = []

    # push(item)
    # 添加一个新的元素item到栈顶
    def push(self, data):
        # 压栈，入栈
        self.__items.append(data)

    # pop()
    # 弹出栈顶元素
    def pop(self):
        # 出栈
        return self.__items.pop()

    # peek()
    # 返回栈顶元素
    def peek(self):
        return self.__items[len(self.__items)-1]

    # is_empty()
    # 判断栈是否为空
    def is_empty(self):
        # if len(self.__items):
        #     return False
        # else:
        #     return True
        return not self.size()

    # size()
    # 返回栈的元素个数
    def size(self):
        return len(self.__items)


if __name__ == "__main__":
    s = Stack()

    print("length: ", s.size())
    print("is_empty: ", s.is_empty())


    for i in range(10):
        s.push(i)


    print(s.pop())
    print(s.pop())
    print(s.pop())

    print("size: ", s.size())


    print(s.peek())
    print(s.peek())
    print(s.peek())





