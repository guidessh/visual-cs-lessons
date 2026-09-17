"""Standard-library regression tests for the dynamic-array lesson."""

import unittest

from dynamic_array import DynamicArray


class DynamicArrayTests(unittest.TestCase):
    def values(self, array):
        return [array[index] for index in range(len(array))]

    def test_append_index_and_resize(self):
        array = DynamicArray()
        for value in [10, 20, 30, 40, 50]:
            array.append(value)
        self.assertEqual(self.values(array), [10, 20, 30, 40, 50])
        self.assertEqual(array._capacity, 8)
        self.assertEqual(array[-1], 50)

    def test_insert_matches_list(self):
        array = DynamicArray()
        expected = [10, 20, 30, 40]
        for value in expected:
            array.append(value)
        array.insert(2, 99)
        expected.insert(2, 99)
        self.assertEqual(self.values(array), expected)

    def test_remove_first_match_and_clear_slot(self):
        array = DynamicArray()
        for value in [10, 20, 20, 30]:
            array.append(value)
        array.remove(20)
        self.assertEqual(self.values(array), [10, 20, 30])
        self.assertIsNone(array._items[len(array)])

    def test_bounds_and_missing_value(self):
        array = DynamicArray()
        with self.assertRaises(IndexError):
            _ = array[0]
        with self.assertRaises(ValueError):
            array.remove(404)

    def test_resize_preserves_reference_identity(self):
        payload = {"title": "original"}
        array = DynamicArray()
        for value in [payload, 20, 30, 40, 50]:
            array.append(value)
        self.assertIs(array[0], payload)


if __name__ == "__main__":
    unittest.main(verbosity=2)
