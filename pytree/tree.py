class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        final_string = ""
        if self.left:
            final_string = self.left.item + " "
        else:
            final_string += "None "
        final_string += self.item
        if self.right:
            final_string += " " + self.right.item
        else:
            final_string += " None"
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
        # special case for head. 
        # TODO probably a way to remove this
        if item == self.head.item:
            temp = self.head
            if self.head.left and self.head.right:
                new_node = self._remove_left_most(self.head.right, self.head)
                new_node.left = self.head.left
                new_node.right = self.head.right
                self.head = new_node

            # no children is easy, just eliminate
            elif not self.head.left and not self.head.right:
                self.head = None
            # one child is also easy, just promote child
            elif self.head.left:
                self.head = self.head.left
            elif self.head.right:
                self.head = self.head.right

            return temp


        return self._delete_node(self.head, item, None)

    def _delete_node(self, node, item, parent):
        # not found?
        if node is None:
            return None

        if node.item == item:
            # 2 children -- replace node with left most right child (the
            # smallest value in the right subtree)
            if node.left and node.right:
                self._two_children(node, parent)
            # no children is easy, just eliminate
            elif not node.left and not node.right:
                self._no_children(node, parent)
            # one child is also easy, just promote child
            else:
                self._one_child(node, parent)

            return node

        if node.item > item:
            return self._delete_node(node.left, item, node)
        else:
            return self._delete_node(node.right, item, node)

    def _no_children(self, node, parent):
        if parent:
            if node == parent.left:
                parent.left = None
            else:
                parent.right = None

    def _one_child(self, node, parent):
        if node.left:
            if parent:
                if node == parent.left:
                    parent.left = node.left
                else:
                    parent.right = node.left
        else:
            if parent:
                if node == parent.left:
                    parent.left = node.right
                else:
                    parent.right = node.right

    def _remove_left_most(self, node, parent):
        if node.left:
            return self._remove_left_most(node.left, node)
        else:
            if node.right:
                self._one_child(node, parent)
                node.right = None
            else:
                self._no_children(node, parent)
            return node

    def _two_children(self, node, parent):
        new_node = self._remove_left_most(node.right, node)
        new_node.left = node.left
        new_node.right = node.right

        if parent:
            if node == parent.left:
                parent.left = new_node
            else:
                parent.right = new_node

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
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting e\n"
    tree.delete("e")
    tree.traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting a\n"
    tree.delete("a")
    tree.traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting pom\n"
    tree.delete("pom")
    tree.traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting b\n"
    tree.delete("b")
    tree.traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting alphabet\n"
    tree.delete("alphabet")
    tree.traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting c\n"
    tree.delete("c")
    tree.traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting zelp\n"
    tree.delete("zelp")
    tree.traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting cass\n"
    tree.delete("cass")
    tree.traverse()
    print
    for i in tree_iterator(tree.head):
        print i
