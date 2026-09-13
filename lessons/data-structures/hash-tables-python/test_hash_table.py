import unittest

from hash_table import HashTable, stable_index


class HashTableTests(unittest.TestCase):
    def test_collision_preserves_both_values(self) -> None:
        table = HashTable(bucket_count=5)
        table.set("Mia", 80)
        table.set("Sam", 55)

        self.assertEqual(stable_index("Mia", 5), 4)
        self.assertEqual(stable_index("Sam", 5), 4)
        self.assertEqual(table.get("Mia"), 80)
        self.assertEqual(table.get("Sam"), 55)

    def test_setting_an_existing_key_updates_in_place(self) -> None:
        table = HashTable(bucket_count=5)
        table.set("Mia", 80)
        table.set("Mia", 91)

        self.assertEqual(table.get("Mia"), 91)
        self.assertEqual(len(table.buckets[4]), 1)

    def test_missing_key_raises_key_error(self) -> None:
        table = HashTable(bucket_count=5)

        with self.assertRaises(KeyError):
            table.get("Ada")


if __name__ == "__main__":
    unittest.main()
