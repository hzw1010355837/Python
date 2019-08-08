



class Queue(object):
    def __init__(self):
        self.__items = []

    # enqueue(item)
    # 往队列中添加一个item元素
    def enqueue(self, data):
        # 入队（尾部）
        self.__items.append(data)


    def enqueue2(self, data):
        # 入队（头部）
        self.__items.insert(0, data)


    # dequeue()
    # 从队列头部删除一个元素
    def dequeue(self):
        # 出队（头部）
        return self.__items.pop(0)


    def dequeue2(self):
        # 出队（尾部）
        return self.__items.pop()

    # is_empty()
    # 判断一个队列是否为空
    def is_empty(self):
        return not self.size()

    # size()
    # 返回队列的大小
    def size(self):
        return len(self.__items)



if __name__ == "__main__":
    q = Queue()

    print("length: ", q.size())
    print("is_empty: ", q.is_empty())

    for i in range(10):
        q.enqueue(i)

    print(q.dequeue())
    print(q.dequeue())

