# Arrays and Python lists: what happens in memory

Companion code for the Guides.sh 3D-animated lesson **Arrays vs Python Lists:
What Really Happens in Memory**.

`DynamicArray` makes capacity growth, indexed access, insertion shifts,
deletion shifts, and reference preservation visible. It is a teaching model,
not CPython's exact list-growth implementation.

Run the example:

```bash
python dynamic_array.py
```

Run the dependency-free regression tests:

```bash
python test_dynamic_array.py
```

The exact compact test shown in the video is preserved as
`lesson_test_pytest.py` and can be run with `python -m pytest
lesson_test_pytest.py` when pytest is installed.

Watch the visual lesson: link added after the scheduled YouTube upload.
