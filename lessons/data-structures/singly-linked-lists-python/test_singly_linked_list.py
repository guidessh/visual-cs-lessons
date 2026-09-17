"""Dependency-free regression tests for the singly linked-list lesson."""

import unittest

from singly_linked_list import LinkedList


def build(values):
    linked = LinkedList()
    for value in values:
        linked.append(value)
    return linked


class SinglyLinkedListTests(unittest.TestCase):
    def test_empty_and_single_node(self):
        linked = LinkedList()
        self.assertEqual(list(linked), [])
        linked.prepend(7)
        node = linked.head
        linked.reverse()
        self.assertIs(linked.head, node)
        self.assertTrue(linked.delete(7))
        self.assertIsNone(linked.head)

    def test_insert_delete_and_search(self):
        linked = build([1, 2, 3])
        linked.insert(1, 9)
        self.assertEqual(list(linked), [1, 9, 2, 3])
        self.assertEqual(linked.search(2).value, 2)
        self.assertTrue(linked.delete(9))
        self.assertFalse(linked.delete(99))
        self.assertEqual(list(linked), [1, 2, 3])

    def test_insert_bounds_preserve_values(self):
        linked = build([1, 2])
        for index in (-1, 3, 99):
            with self.assertRaises(IndexError):
                linked.insert(index, 8)
            self.assertEqual(list(linked), [1, 2])

    def test_reverse_preserves_node_identity(self):
        linked = build([4, 18, 11, 27, 39])
        original = []
        node = linked.head
        while node:
            original.append(node)
            node = node.next
        linked.reverse()
        reversed_nodes = []
        node = linked.head
        while node:
            reversed_nodes.append(node)
            node = node.next
        self.assertEqual(reversed_nodes, original[::-1])
        self.assertEqual(list(linked), [39, 27, 11, 18, 4])


if __name__ == "__main__":
    unittest.main(verbosity=2)
