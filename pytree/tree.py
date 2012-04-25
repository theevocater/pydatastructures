class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        final_string = ""
        if self.left:
            final_string = self.left.item + " "
        final_string += self.item
        if self.right:
            final_string += " " + self.right.item
        return final_string

class Tree:
    def __init__(self):
        self.head = None
        
    #def __str__(self):
        #self.traverse()

    def push(self, item):
        if self.head is None:
            self.head = Node(item)
            return self.head

        return self.__createNode(self.head, item, None, False)

    def __createNode(self, node, item, parent, left):
        if node is None:
            node = Node(item)
            if left:
                parent.left = node
            else:
                parent.right = node
            return node

        if node.item > item:
            return self.__createNode(node.left, item, node, True)
        else:
            return self.__createNode(node.right, item, node, False)

    def delete(self, item):
        if not self.head:
            return None

        return self.__deleteNode()

    def __leftMost(self, node):
        if node.left:
            return self.__leftMost(node.left)
        else:
            return node

    def __deleteNode(self, node, item, parent, left):
        # not found?
        if node is None:
            return None

# TODO deal with deletion
        if node.item == item:
            if left:
                parent.left = node
            else:
                parent.right = node
            return node

        if node.item > item:
            return self.__createNode(node.left, item, node, True)
        else:
            return self.__createNode(node.right, item, node, False)

    def traverse(self):
        self.__traverse(self.head)
        
    def __traverse(self, node):
        if node is None:
            return
        self.__traverse(node.left)
        print str(node)
        self.__traverse(node.right)

def tree_iterator(node):
    if node:
        for x in tree_iterator(node.left):
            yield x
        yield node.item
        for x in tree_iterator(node.right):
            yield x


tree = Tree()
tree.push("b")
tree.push("c")
tree.push("a")
tree.push("e")
tree.push("alphabet")
tree.push("zelp")
tree.push("pom")
tree.push("cass")
tree.traverse()
for i in tree_iterator(tree.head):
    print i
