# Hash Tables for Beginners in Python

Companion code for **Hash Tables for Beginners: 3D Animated Step by Step**.

Run the example:

```bash
python hash_table.py
```

Run the tests:

```bash
python -m unittest -v test_hash_table.py
```

The stable hash is intentionally simple and keeps `Mia` and `Sam` in bucket 4
on every run. Production hash functions are more sophisticated, and Python
randomizes its built-in string hash between processes.
