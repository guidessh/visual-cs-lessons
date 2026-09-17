import pytest

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


def test_every_boundary():
    chain = DoublyLinkedList()
    assert_chain(chain, [])
    middle = chain.append(20)
    assert_chain(chain, [20])
    head = chain.prepend(10)
    assert_chain(chain, [10, 20])
    tail = chain.append(40)
    assert_chain(chain, [10, 20, 40])
    inserted = chain.insert_after(middle, 30)
    assert_chain(chain, [10, 20, 30, 40])
    assert chain.delete(inserted) == 30
    assert_chain(chain, [10, 20, 40])
    chain.delete(head)
    assert_chain(chain, [20, 40])
    chain.delete(tail)
    assert_chain(chain, [20])
    chain.delete(middle)
    assert_chain(chain, [])
    assert middle.prev is None and middle.next is None
    assert middle._owner is None


def test_empty_prepend_and_insert_after_tail():
    chain = DoublyLinkedList()
    first = chain.prepend(7)
    assert_chain(chain, [7])
    second = chain.insert_after(first, 7)
    assert_chain(chain, [7, 7])
    assert second is chain.tail and second is not first
    chain.delete(first)
    assert_chain(chain, [7])
    chain.delete(second)
    assert_chain(chain, [])


def test_reject_foreign_and_deleted_nodes():
    chain = DoublyLinkedList()
    member = chain.append(1)
    foreign = DoublyLinkedList().append(2)
    detached = DoublyNode(3)
    for invalid in (foreign, detached, None):
        with pytest.raises(ValueError):
            chain.insert_after(invalid, 4)
        with pytest.raises(ValueError):
            chain.delete(invalid)
        assert_chain(chain, [1])
    chain.delete(member)
    assert_chain(chain, [])
    with pytest.raises(ValueError):
        chain.delete(member)
    assert_chain(chain, [])
