"""A doubly linked list with constant-time operations on a known member node.

Nodes are handles: callers may read links but must mutate through the list.
The ownership token rejects foreign/deleted handles without a linear search.
Iteration assumes the list is not mutated during traversal.
"""

from dataclasses import dataclass, field


@dataclass(eq=False, slots=True)
class DoublyNode:
    value: object
    prev: "DoublyNode | None" = None
    next: "DoublyNode | None" = None
    _owner: object | None = field(default=None, repr=False)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
        self._token = object()

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __reversed__(self):
        current = self.tail
        while current is not None:
            yield current.value
            current = current.prev

    def _require_member(self, node):
        if not isinstance(node, DoublyNode) or node._owner is not self._token:
            raise ValueError("node is not a member of this list")

    def prepend(self, value):
        new_node = DoublyNode(value, _owner=self._token)
        new_node.next = self.head
        if self.head is None:
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node
        self._size += 1
        return new_node

    def append(self, value):
        new_node = DoublyNode(value, _owner=self._token)
        new_node.prev = self.tail
        if self.tail is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self._size += 1
        return new_node

    def insert_after(self, node, value):
        self._require_member(node)
        if node is self.tail:
            return self.append(value)
        right = node.next
        new_node = DoublyNode(value, _owner=self._token)
        new_node.prev = node
        new_node.next = right
        node.next = new_node
        right.prev = new_node
        self._size += 1
        return new_node

    def delete(self, node):
        self._require_member(node)
        left = node.prev
        right = node.next
        if left is None:
            self.head = right
        else:
            left.next = right
        if right is None:
            self.tail = left
        else:
            right.prev = left
        node.prev = None
        node.next = None
        node._owner = None
        self._size -= 1
        return node.value


def demo():
    history = DoublyLinkedList()
    home = history.append("Home")
    lesson = history.append("Lesson")
    history.append("Practice")
    quiz = history.insert_after(lesson, "Quiz")
    print("Forward:", list(history))
    print("Backward:", list(reversed(history)))
    history.delete(quiz)
    history.delete(home)
    print("After deletion:", list(history))
    print("Back to:", history.tail.prev.value)
    assert list(history) == ["Lesson", "Practice"]
    assert history.head.prev is None and history.tail.next is None


if __name__ == "__main__":
    demo()
