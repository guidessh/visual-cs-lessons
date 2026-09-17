"""A head-only singly linked list for the Guides pointer lesson."""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def prepend(self, value):
        node = Node(value, self.head)
        self.head = node

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def insert(self, index, value):
        if index < 0:
            raise IndexError("insertion index out of range")
        if index == 0:
            self.prepend(value)
            return
        previous = self.head
        for _ in range(index - 1):
            if previous is None:
                raise IndexError("insertion index out of range")
            previous = previous.next
        if previous is None:
            raise IndexError("insertion index out of range")
        node = Node(value, previous.next)
        previous.next = node

    def delete(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        previous = self.head
        while previous.next is not None:
            if previous.next.value == value:
                previous.next = previous.next.next
                return True
            previous = previous.next
        return False

    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous


if __name__ == "__main__":
    linked = LinkedList()
    for value in (18, 21, 27):
        linked.append(value)
    print("Start:", list(linked))
    linked.prepend(4)
    linked.append(39)
    linked.insert(2, 11)
    print("Inserted:", list(linked))
    print("Deleted 21:", linked.delete(21))
    print("After delete:", list(linked))
    found = linked.search(27)
    print("Search 27:", found.value if found is not None else None)
    linked.reverse()
    print("Reversed:", list(linked))
    print("Missing 99:", linked.delete(99))
