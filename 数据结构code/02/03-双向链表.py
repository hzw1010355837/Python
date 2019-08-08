


# 双向链表的结构特征
# 节点：数据、向前引用、向后引用
# 头节点的向前引用为空、尾部节点的向后引用为空


class Node(object):
    def __init__(self, data):
        self.data = data
        self.pre = None
        self.next = None



class DLinkList(object):
    def __init__(self):
        self.__head = None

    # is_empty() 链表是否为空
    def is_empty(self):
        return not self.__head


    # add(data) 链表头部添加元素
    def add(self, data):
        node = Node(data)

        if self.is_empty():
            self.__head = node
            return

        node.next = self.__head
        self.__head.pre = node
        self.__head = node

    # show() 遍历整个链表
    def show(self):
        cur = self.__head
        while cur != None:

            print(cur.data, end=" --> ")

            cur = cur.next

        print("None")

    # append(data) 链表尾部添加元素
    def append(self, data):
        if self.is_empty():
            self.add(data)
            return

        # 找到尾部节点
        cur = self.__head
        while cur.next != None:
            cur = cur.next

        # cur指向到就是尾部节点
        node = Node(data)
        node.pre = cur
        cur.next = node


    # length() 链表长度
    def length(self):
        num = 0
        cur = self.__head
        while cur != None:
            num += 1
            cur = cur.next

        return num

    # search(data) 查找节点是否存在
    def search(self, data):
        cur = self.__head
        while cur != None:

            # cur是一个有效到节点
            if cur.data == data:
                return True

            cur = cur.next

        return False

    # remove(data) 删除节点
    def remove(self, data):
        cur = self.__head
        while cur != None:
            # cur指向的是一个有效的节点
            if cur.data == data:
                # 当前cur就是要删除的节点

                if cur == self.__head:
                    # cur恰恰好是头部节点
                    self.__head = cur.next
                    if self.__head:
                        self.__head.pre = None
                    return

                if cur.next == None:
                    # cur恰恰好是尾节点
                    cur.pre.next = cur.next # None
                    return


                cur.pre.next = cur.next
                cur.next.pre = cur.pre
                return

            cur = cur.next


    # insert(index, data) 指定位置添加元素
    def inert(self, index, data):
        # index <=0 头部插入
        if index <= 0:
            self.add(data)
            return

        # index > self.length()-1 添加尾部
        if index > self.length() - 1:
            self.append(data)
            return


        # 普通中间部分插入

        # 通过偏移找到index的前置节点
        cur = self.__head
        for i in range(index-1):
            cur = cur.next

        # cur就是index的前置节点
        node = Node(data)

        node.next = cur.next
        node.pre = cur
        cur.next.pre = node
        cur.next = node



if __name__ == "__main__":
    s = DLinkList()


    s.add(1)
    s.add(2)
    s.add(3)

    s.show()

    print("length: ", s.length())

    print(" ------- ")
    s.append([1,2])
    s.show()

    print("search: ", s.search([1,2,5]))

    print(" ------ ")
    s.remove(3)
    s.show()

    print(" ------ ")

    s.inert(1, 999)
    s.show()