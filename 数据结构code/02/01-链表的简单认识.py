









# 定义出链表的节点数据类型
class Node(object):
    def __init__(self, data):
        # 数据域
        self.data = data
        # 引用域
        self.next = None



if __name__ == "__main__":
    node1 = Node(12345)
    node2 = Node("abcde")
    node3 = Node([1,2])
    node4 = Node((4,5))

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4


    print(head.data)
    print(head.next.data)
    print(head.next.next.data)
    print(head.next.next.next.data)