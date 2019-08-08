


# 单向循环链表的结构特征
# 节点：数据、向后引用
# 尾部节点的向后引用，指向的是头部节点

# 定义出链表的节点数据类型
class Node(object):
    def __init__(self, data):
        # 数据域
        self.data = data
        # 引用域
        self.next = None


class SinCycLinkedlist(object):
    def __init__(self):
        self.__head = None

    # is_empty() 链表是否为空
    def is_empty(self):
        return not self.__head

    # add(item) 链表头部添加元素
    def add(self, data):
        node = Node(data)

        if self.is_empty():
            self.__head = node
            node.next = self.__head
            return

        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next

        # cur指向的就是尾部节点


        node.next = self.__head
        self.__head = node
        cur.next = self.__head

    # show() 遍历整个链表
    def show(self):
        if self.is_empty():
            print("空链表")
            return

        cur = self.__head
        while cur.next != self.__head:
            print(cur.data, end=" --> ")
            cur = cur.next

        # cur指向的是尾部
        print(cur.data, end=" --> ")
        print("<head>")


    # append(data) 链表尾部添加元素
    def append(self, data):
        if self.is_empty():
            self.add(data)
            return

        # 找到尾部节点
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next

        node = Node(data)
        cur.next = node
        node.next = self.__head

    # length() 链表长度
    def length(self):
        if self.is_empty():
            return 0

        num = 0
        cur = self.__head
        while cur.next != self.__head:
            # cur不是尾部节点
            num += 1
            cur = cur.next

        return num+1

    # search(data) 查找节点是否存在
    def search(self, data):
        if self.is_empty():
            return False

        cur = self.__head
        while cur.next != self.__head:
            # cur不是尾部节点
            if cur.data == data:
                return True
            cur = cur.next

        if cur.data == data:
            return True

        return False


    # remove(data) 删除节点
    def remove(self, data):
        if self.is_empty():
            return

        cur = self.__head
        pre = None

        while cur.next != self.__head:
            # pre指向的是cur的前置节点

            if cur.data == data:
                # cur指向的就是我们要删除的节点
                if cur == self.__head:
                    # cur指向头节点，正好是要删除的节点

                    # 找到原来的尾部节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    # rear指向的就是尾部节点
                    self.__head = cur.next
                    rear.next = self.__head
                    return

                pre.next = cur.next
                return

            pre = cur
            cur = cur.next


        # cur指向的是尾部节点
        if cur.data == data:
            if cur == self.__head:
                self.__head = None
                return
            pre.next = cur.next
            return



    # insert(index, data) 指定位置添加元素
    def insert(self, index, data):
        # 如果index<=0，插入头部
        if index <= 0:
            self.add(data)
            return

        # 如果index越界，追加到尾部
        if index > self.length() - 1:
            self.append(data)
            return

        cur = self.__head
        # 偏移index-1次
        for i in range(index - 1):
            cur = cur.next
        # cur指向的就是插入位置index的前置节点
        node = Node(data)
        node.next = cur.next
        cur.next = node




if __name__ == "__main__":
    s = SinCycLinkedlist()

    # s.add(1)
    # s.add(2)
    # s.add(3)

    # s.show()

    print(" ------- ")
    # s.append([1,2])
    # s.show()

    # print("length: ", s.length())

    print(" ------ ")
    s.insert(-9, 999)
    # s.insert(10000, 888)
    # s.insert(3, 777)
    s.show()

    print(" ------- ")
    s.remove(999)
    s.show()