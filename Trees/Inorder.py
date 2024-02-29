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

def Inordertraversal(rootnode):
    if not rootnode:
        return
    Inordertraversal(rootnode.leftchild)
    print(rootnode.data)
    Inordertraversal(rootnode.rightchild)

Inordertraversal(node_BT)
