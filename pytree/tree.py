class Node:
    def __init__(self, item):
        """
            Creates a new node with data item "item"
        """
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        """
            returns a representation of the node which is
            str(left.item) + str(item) + str(right.item)
        """
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
    def __init__(self, item=None):
        """
            Initializes a tree with an element
        """
        self.head = None
        if item:
            self.insert(item)

    def search(self, item):
        """
            Searches for a given item in the tree. Mostly useful if you
            redefine the __eq__()
        """
        return self._search(self.head, item)

    def _search(self, node, item):
        if node is None:
            return None

        if node.item == item:
            return node.item

        if item < node.item:
            return self._search(node.left, item)

        return self._search(node.right, item)

    def insert(self, item):
        """
            Inserts a new node into the tree
        """
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
        """
            Deletes a node from the tree
        """
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

    def inorder_traverse(self):
        """
            Returns an inorder str(item) traversal of the tree.
        """
        return self._inorder_traverse(self.head)

    def _inorder_traverse(self, node):
        if node is None:
            return ""
        return self._inorder_traverse(node.left) + " " + str(node.item) \
                + self._inorder_traverse(node.right)


def tree_iterator(node):
    if node:
        for x in tree_iterator(node.left):
            yield x
        yield node.item
        for x in tree_iterator(node.right):
            yield x


if __name__ == "__main__":
    tree = Tree()
    tree.insert("b")
    tree.insert("c")
    tree.insert("a")
    tree.insert("e")
    tree.insert("alphabet")
    tree.insert("zelp")
    tree.insert("pom")
    tree.insert("cass")
    print "Search Test"
    print "Search for b"
    print tree.search("b")
    print "Searching for nop"
    print tree.search("nop")
    print
    print tree.inorder_traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting e\n"
    tree.delete("e")
    print tree.inorder_traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting a\n"
    tree.delete("a")
    print tree.inorder_traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting pom\n"
    tree.delete("pom")
    print tree.inorder_traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting b\n"
    tree.delete("b")
    print tree.inorder_traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting alphabet\n"
    tree.delete("alphabet")
    print tree.inorder_traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting c\n"
    tree.delete("c")
    print tree.inorder_traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting zelp\n"
    tree.delete("zelp")
    print tree.inorder_traverse()
    print
    for i in tree_iterator(tree.head):
        print i
    print "\ndeleting cass\n"
    tree.delete("cass")
    print tree.inorder_traverse()
    print
    for i in tree_iterator(tree.head):
        print i
