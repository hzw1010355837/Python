



class Queue(object):
    def __init__(self):
        self.__items = []


    def enqueue(self, data):
        self.__items.append(data)

    def dequeue(self):
        return self.__items.pop(0)

    def is_empty(self):
        return not len(self.__items)


# 二叉树节点类
# 数据、左引用、右引用

class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

# 完全二叉树
class BinaryTree(object):
    def __init__(self):
        self.__root = None # 一颗树的根节点

    def get_root(self):
        return self.__root

    # add(data) -- 添加一条数据
    def add(self, data):
        node = Node(data)

        # 空树
        if self.__root == None:
            self.__root = node
            return

        q = Queue()
        q.enqueue(self.__root)


        while True:

            # 取一个节点
            root = q.dequeue()

            # 判断该节点的左右子节点是否为空 --- 空，就是合适的插入位置
            if root.lchild == None:
                 root.lchild = node
                 return
            q.enqueue(root.lchild)

            if root.rchild == None:
                root.rchild = node
                return
            q.enqueue(root.rchild)


    # show() -- 遍历
    def show(self):
        q = Queue()
        q.enqueue(self.__root)

        while not q.is_empty():
            # if q.is_empty():
            #     break

            # 取一个节点
            root = q.dequeue()

            print(root.data)

            if root.lchild:
                q.enqueue(root.lchild)
            if root.rchild:
                q.enqueue(root.rchild)


    # search(data) -- 查找
    def search(self, data):
        q = Queue()
        q.enqueue(self.__root)

        while not q.is_empty():
            # if q.is_empty():
            #     break

            # 取一个节点
            root = q.dequeue()

            # print(root.data)
            if root.data == data:
                return True

            if root.lchild:
                q.enqueue(root.lchild)
            if root.rchild:
                q.enqueue(root.rchild)

        return False


def preorder(root):
    if root == None:
        return

    # 前序遍历， 根，左，右
    print(root.data)
    preorder(root.lchild)
    preorder(root.rchild)


def preordersearch(root, data):
    # 前序遍历查找
    if root == None:
        return False

    isTrue1 = False
    isTrue2 = False
    isTrue3 = False

    # 前序遍历， 根，左，右
    if root.data == data:
        isTrue1 =True

    isTrue2 = preordersearch(root.lchild, data)
    isTrue3 = preordersearch(root.rchild, data)

    return isTrue1 or isTrue2 or isTrue3


def midorder(root):
    if root == None:
        return

    midorder(root.lchild)
    print(root.data)
    midorder(root.rchild)

def postorder(root):
    if root == None:
        return

    postorder(root.lchild)
    postorder(root.rchild)
    print(root.data)




if __name__ == "__main__":
    # node1 = Node("A")
    # node2 = Node("B")
    # node3 = Node("C")
    #
    # root = node1
    # node1.lchild = node2
    # node1.rchild = node3
    #
    #
    # node4 = Node("D")
    # node2.lchild = node4
    #
    #
    #
    # # root
    # print(root.data)
    # print(root.lchild.data)
    # print(root.rchild.data)
    # print(root.lchild.lchild.data)

    t = BinaryTree()

    for i in range(10):
        t.add(i)

    # t.show()

    # print(t.search(99))

    # postorder(t.get_root())

    print(preordersearch(t.get_root(), 99))
