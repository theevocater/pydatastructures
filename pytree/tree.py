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

        return self._create_node(self.head, item, None, False)

    def _create_node(self, node, item, parent, left):
        if node is None:
            node = Node(item)
            if left:
                parent.left = node
            else:
                parent.right = node
            return node

        if node.item > item:
            return self._create_node(node.left, item, node, True)
        else:
            return self._create_node(node.right, item, node, False)

    def delete(self, item):
        if not self.head:
            return None

        return self._delete_node()

    def _left_most(self, node):
        if node.left:
            return self._left_most(node.left)
        else:
            return node

    def _delete_node(self, node, item, parent, left):
        # not found?
        if node is None:
            return None

        if node.item == item:
            # 2 children -- replace node with left most right child (the
            # smallest value in the right subtree)
            # TODO: finish _left_most.  probably want the parent as well.
            if node.left and node.right:
                if left:
                    parent.left = node
                else:
                    parent.right = node
            # no children is easy, just eliminate
            if not node.left and not node.right:
                if left:
                    parent.left = None
                else:
                    parent.right = None
            # one child is also easy, just promote child
            else:
                if node.left:
                    if left:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                else:
                    if left:
                        parent.left = node.right
                    else:
                        parent.right = node.right

            return node

        if node.item > item:
            return self._delete_node(node.left, item, node, True)
        else:
            return self._delete_node(node.right, item, node, False)

    def _no_children():
        pass

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


if __name__ == "__main__":
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
