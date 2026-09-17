"""A teaching array: fixed-length storage, explicit growth, Python-style indices.

This demonstrates a dynamic-array policy, not CPython's list implementation.
The backing list never grows in place. Slicing and mutation inside __eq__ are
outside this small API; remove(value) deletes the first matching value.
"""

from operator import index as integer_index


class DynamicArray:
    def __init__(self):
        self._size = 0
        self._capacity = 4
        self._items = [None] * self._capacity

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        index = integer_index(index)
        if index < 0:
            index += self._size
        if not 0 <= index < self._size:
            raise IndexError("array index out of range")
        return self._items[index]

    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._items[self._size] = value
        self._size += 1

    def insert(self, index, value):
        index = integer_index(index)
        if index < 0:
            index = max(0, self._size + index)
        index = min(index, self._size)
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        for position in range(self._size, index, -1):
            self._items[position] = self._items[position - 1]
        self._items[index] = value
        self._size += 1

    def remove(self, value):
        for index in range(self._size):
            if self._items[index] is value or self._items[index] == value:
                for position in range(index, self._size - 1):
                    self._items[position] = self._items[position + 1]
                self._size -= 1
                self._items[self._size] = None
                return
        raise ValueError("value not in array")

    def _resize(self, capacity):
        if capacity < max(1, self._size):
            raise ValueError("capacity cannot discard live items")
        replacement = [None] * capacity
        for index in range(self._size):
            replacement[index] = self._items[index]
        self._items = replacement
        self._capacity = capacity


def main():
    array = DynamicArray()
    builtin = []
    for value in [10, 20, 30, 40, 50]:
        array.append(value)
        builtin.append(value)
    array.insert(2, 99)
    builtin.insert(2, 99)
    array.remove(20)
    builtin.remove(20)
    actual = [array[index] for index in range(len(array))]
    assert actual == builtin
    assert array[-1] == builtin[-1] == 50
    print("values:", actual)
    print("length:", len(array), "capacity:", array._capacity)
    print("Python list parity: passed")


if __name__ == "__main__":
    main()
