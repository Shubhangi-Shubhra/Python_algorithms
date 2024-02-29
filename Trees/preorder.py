class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

# Creating an instance of TreeNode
node_BT = TreeNode("a")
lc = TreeNode("b")
rc = TreeNode("c")
node_BT.left_child = lc
node_BT.right_child = rc

def preordertraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preordertraversal(rootnode.left_child)
    preordertraversal(rootnode.right_child)
preordertraversal(node_BT)    
    