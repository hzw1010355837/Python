


# 单向链表的结构特征
# 节点：数据、引用
# 尾部节点的next指向None


# 定义出链表的节点数据类型
class Node(object):
    def __init__(self, data):
        # 数据域
        self.data = data
        # 引用域
        self.next = None




class SingleLinkList(object):
    def __init__(self):
        self.__head = None

    # is_empty() 链表是否为空
    def is_empty(self):
        # if self.__head == None:
        #     return True
        # return False
        return not self.__head


    # add(data) 链表头部添加元素
    def add(self, data):
        node = Node(data)

        node.next = self.__head
        self.__head = node


    # show() 遍历整个链表
    def show(self):
        cur = self.__head

        # while True:
            # if cur == None:
            #     break
        while cur != None:
            # 当cur不为None，说明cur指向当前节点是一个有效节点
            print(cur.data, end=' --> ')

            cur = cur.next

        print("None")


    # append(data) 链表尾部添加元素
    def append(self, data):

        if self.is_empty():
            self.add(data)
            return


        # 找到原来的尾部节点
        cur = self.__head
        while cur.next != None:
            # if cur.next == None:
                # cur指向的就是尾部节点
                # break
            cur = cur.next


        # cur就是尾部节点
        node = Node(data)
        cur.next = node


    # length() 链表长度
    def length(self):
        # 本质就是在遍历的过程当中，如果当前节点是有效节点就累加

        # 记录有效节点
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

            if cur.data == data:
                return True

            cur = cur.next

        return False


    # remove(data) 删除节点
    def remove(self, data):
        cur = self.__head
        pre = None
        while cur != None:
            # cur指向当前节点，pre指向cur的前置节点

            if cur.data == data:
                # cur就是我们要删除的节点

                # 如果删除的是头节点，特殊处理
                if cur == self.__head:
                    self.__head = self.__head.next
                    return

                # pre.next = cur.next
                pre.next = cur.next
                return

            pre = cur
            cur = cur.next


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
        for i in range(index-1):
            cur = cur.next
        # cur指向的就是插入位置index的前置节点
        node = Node(data)
        node.next = cur.next
        cur.next = node



if __name__ == "__main__":

    # 定义了一个空链表
    s = SingleLinkList()


    s.add(1)
    s.add(2)
    s.add(3)
    s.add(4)
    s.add(5)

    s.show()
    print(" ------- ")

    s.append([1,2])
    s.show()

    print("length: ", s.length())

    print("search: ", s.search([1,2,4]))

    print(" ------- ")
    s.remove(3)
    s.show()

    print(" ------- ")
    s.insert(999999, 999)
    s.show()
