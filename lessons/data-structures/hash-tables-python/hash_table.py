"""Small deterministic hash table with repeatable string indexes.

Python's built-in ``hash()`` is intentionally randomized between processes for
strings. ``stable_index`` keeps each key assigned to the same bucket between
runs.
"""


def stable_index(key: str, bucket_count: int) -> int:
    return sum(ord(character) for character in key) % bucket_count


class HashTable:
    def __init__(self, bucket_count: int = 5) -> None:
        if bucket_count < 1:
            raise ValueError("bucket_count must be positive")
        self.buckets: list[list[tuple[str, int]]] = [
            [] for _ in range(bucket_count)
        ]

    def index_for(self, key: str) -> int:
        return stable_index(key, len(self.buckets))

    def set(self, key: str, value: int) -> None:
        bucket = self.buckets[self.index_for(key)]

        for position, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[position] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key: str) -> int:
        bucket = self.buckets[self.index_for(key)]

        for stored_key, value in bucket:
            if stored_key == key:
                return value

        raise KeyError(key)


if __name__ == "__main__":
    scores = HashTable(bucket_count=5)
    scores.set("Mia", 80)
    scores.set("Sam", 55)

    print("Mia index:", scores.index_for("Mia"))
    print("Sam index:", scores.index_for("Sam"))
    print("Bucket 4:", scores.buckets[4])
    print("Sam's score:", scores.get("Sam"))
