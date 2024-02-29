import queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

node_BT = TreeNode("A")
Lc = TreeNode("B")
Rc = TreeNode("C")
node_BT.leftchild = Lc  # Assigning left child
node_BT.rightchild = Rc  # Assigning right child

def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.put(rootNode)  # Use put() to enqueue
        while not customQueue.empty():  # Use empty() to check if the queue is empty
            root = customQueue.get()  # Use get() to dequeue
            print(root.data)
            if root.leftchild is not None:
                customQueue.put(root.leftchild)
            if root.rightchild is not None:
                customQueue.put(root.rightchild)

def search(rootNode, nodevalue):
    if not rootNode:
        return "BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.put(rootNode)
        while not customQueue.empty():
            root = customQueue.get()
            if root.data == nodevalue:
                return "Success"
            if root.leftchild is not None:
                customQueue.put(root.leftchild)
            if root.rightchild is not None:
                customQueue.put(root.rightchild)
    return "Node not found"

print(search(node_BT, "A"))
