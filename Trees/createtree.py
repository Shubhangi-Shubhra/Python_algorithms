class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children if children is not None else []

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, child_node):
        self.children.append(child_node)

# Example usage:
tree = TreeNode('Drinks', [])
cold = TreeNode('Cold')
hot = TreeNode('Hot')
tree.add_child(cold)
tree.add_child(hot)

print(tree)
