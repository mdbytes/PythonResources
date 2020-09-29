
class BinaryTree:

    def __init__(self, root_object):
        self.key = root_object
        self.left_child = None
        self.right_child = None

    def insertLeft(self,new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insertRight(self,new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def getRightChild(self):
        return self.right_child

    def getLeftChild(self):
        return self.left_child

    def setRootValue(self, root_object):
        self.key = root_object

    def getRootValue(self):
        return self.key


bin_tree = BinaryTree('a')

bin_tree.insertLeft('b')

bin_tree.insertRight('c')

print(bin_tree.getRootValue())
print(bin_tree.getLeftChild())
print(bin_tree.getLeftChild().getRootValue())
print(bin_tree.getRightChild().getRootValue())