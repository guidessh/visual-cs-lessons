import pytest

from singly_linked_list import LinkedList, Node


def make_list(values):
    linked = LinkedList()
    for value in values:
        linked.append(value)
    return linked


def nodes(linked):
    result = []
    current = linked.head
    while current is not None:
        assert current not in result, "cycle detected"
        result.append(current)
        current = current.next
    return result


def test_empty_list():
    linked = LinkedList()
    assert linked.head is None
    assert list(linked) == []
    assert linked.search(1) is None
    assert linked.delete(1) is False
    linked.reverse()
    assert linked.head is None


@pytest.mark.parametrize("operation", ["prepend", "append"])
def test_single_node(operation):
    linked = LinkedList()
    getattr(linked, operation)(7)
    original = linked.head
    assert isinstance(original, Node)
    assert original.next is None
    linked.reverse()
    assert linked.head is original
    assert linked.search(7) is original
    assert linked.delete(7) is True
    assert linked.head is None


@pytest.mark.parametrize("index, expected", [(0, [9, 1, 2, 3]), (1, [1, 9, 2, 3]), (3, [1, 2, 3, 9])])
def test_insert_head_middle_tail(index, expected):
    linked = make_list([1, 2, 3])
    before = nodes(linked)
    linked.insert(index, 9)
    assert list(linked) == expected
    assert [node for node in nodes(linked) if node.value != 9] == before


def test_insert_into_empty():
    linked = LinkedList()
    linked.insert(0, 8)
    assert list(linked) == [8]
    assert linked.head.next is None


@pytest.mark.parametrize("values, index", [([], -1), ([], 1), ([1], -1), ([1], 2), ([1, 2], 99)])
def test_insert_bounds_preserve_list(values, index):
    linked = make_list(values)
    before = nodes(linked)
    with pytest.raises(IndexError, match="insertion index out of range"):
        linked.insert(index, 99)
    assert nodes(linked) == before
    assert list(linked) == values


@pytest.mark.parametrize("value, expected", [(1, [2, 3]), (2, [1, 3]), (3, [1, 2])])
def test_delete_head_middle_tail(value, expected):
    linked = make_list([1, 2, 3])
    before = nodes(linked)
    assert linked.delete(value) is True
    assert list(linked) == expected
    assert nodes(linked) == [node for node in before if node.value != value]


def test_delete_missing_and_first_duplicate():
    linked = make_list([2, 1, 2])
    before = nodes(linked)
    assert linked.delete(99) is False
    assert nodes(linked) == before
    assert linked.search(2) is before[0]
    assert linked.delete(2) is True
    assert nodes(linked) == before[1:]
    assert linked.search(2) is before[2]


@pytest.mark.parametrize("values", [[], [1], [1, 2], [18, 21, 27, 4]])
def test_reverse_preserves_nodes_and_is_involution(values):
    linked = make_list(values)
    before = nodes(linked)
    linked.reverse()
    assert nodes(linked) == before[::-1]
    assert list(linked) == values[::-1]
    linked.reverse()
    assert nodes(linked) == before
    assert list(linked) == values


def test_mixed_operations_match_python_list():
    linked = LinkedList()
    expected = []
    for value in range(12):
        linked.append(value)
        expected.append(value)
        assert list(linked) == expected
    for index, value in [(0, 30), (6, 31), (14, 32)]:
        linked.insert(index, value)
        expected.insert(index, value)
        assert list(linked) == expected
    for value in [30, 6, 32, 99]:
        found = value in expected
        assert linked.delete(value) is found
        if found:
            expected.remove(value)
        assert list(linked) == expected
    linked.reverse()
    expected.reverse()
    assert list(linked) == expected
    assert len(nodes(linked)) == len(expected)
