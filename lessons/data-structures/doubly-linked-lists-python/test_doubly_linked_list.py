"""Dependency-free regression checks for the doubly linked list lesson."""

from doubly_linked_list import DoublyLinkedList, DoublyNode


def assert_chain(chain, expected):
    assert list(chain) == expected
    assert list(reversed(chain)) == expected[::-1]
    assert len(chain) == len(expected)
    if not expected:
        assert chain.head is None and chain.tail is None
        return
    assert chain.head.prev is None
    assert chain.tail.next is None
    previous = None
    current = chain.head
    for value in expected:
        assert current is not None
        assert current.value == value
        assert current.prev is previous
        assert current._owner is chain._token
        if previous is not None:
            assert previous.next is current
        previous = current
        current = current.next
    assert current is None and previous is chain.tail


def expect_value_error(operation):
    try:
        operation()
    except ValueError:
        return
    raise AssertionError("expected ValueError")


def run_tests():
    chain = DoublyLinkedList()
    assert_chain(chain, [])
    middle = chain.append(20)
    head = chain.prepend(10)
    tail = chain.append(40)
    inserted = chain.insert_after(middle, 30)
    assert_chain(chain, [10, 20, 30, 40])
    assert chain.delete(inserted) == 30
    chain.delete(head)
    chain.delete(tail)
    assert_chain(chain, [20])

    foreign = DoublyLinkedList().append(2)
    detached = DoublyNode(3)
    for invalid in (foreign, detached, None):
        expect_value_error(lambda invalid=invalid: chain.insert_after(invalid, 4))
        expect_value_error(lambda invalid=invalid: chain.delete(invalid))
    chain.delete(middle)
    assert_chain(chain, [])
    expect_value_error(lambda: chain.delete(middle))
    print("doubly-linked-list tests passed")


if __name__ == "__main__":
    run_tests()
