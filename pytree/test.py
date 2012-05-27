#!/usr/bin/env python3

import unittest
from tree import Tree
from copy import copy

# TODO consider adding a 'list' of items to add and then adding them randomly
# then deleting
insert_queue = ["b", "c", "a", "e", "alphabet", "zelp", "pom", "cass"]


class Testing(unittest.TestCase):
    def testInsert(self):
        tree = Tree()
        temp = "b"
        tree.insert(temp)
        self.assertEqual(tree.head.item, temp)
        temp = "a"
        tree.insert(temp)
        self.assertEqual(tree.head.left.item, temp)
        temp = "cat"
        tree.insert(temp)
        self.assertEqual(tree.head.right.item, temp)

    def testSearch(self):
        tree = Tree()
        for word in insert_queue:
            tree.insert(word)

        for i in insert_queue:
            self.assertEqual(tree.search(i), i)

        self.assertEqual(tree.search("not found"), None)

    def testDelete(self):
        tree = Tree()
        copy_q = copy(insert_queue)
        for word in copy_q:
            tree.insert(word)

        tree.delete(copy_q[-1])
        self.assertEqual(tree.search(copy_q[-1]), None)

        copy_q.pop()
        copy_q.sort()
        self.assertEqual(tree.inorder_traverse(), " ".join(copy_q))

    def testTraverse(self):
        tree = Tree()
        for word in insert_queue:
            tree.insert(word)

        insert_queue.sort()
        self.assertEqual(tree.inorder_traverse(), " ".join(insert_queue))

unittest.main()
