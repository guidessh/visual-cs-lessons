"""The compact, line-by-line test demo shown in the lesson."""

import pytest

from dynamic_array import DynamicArray


def test_dynamic_array():
    array = DynamicArray()
    expected = [10, 20, 30, 40, 50]
    for value in expected:
        array.append(value)
    assert len(array) == 5
    assert array._capacity == 8
    assert array[2] == 30
    assert array[-1] == 50
    array.insert(2, 99)
    expected.insert(2, 99)
    array.remove(20)
    expected.remove(20)
    assert [array[i] for i in range(len(array))] == expected
    with pytest.raises(IndexError):
        _ = array[len(array)]
    with pytest.raises(ValueError):
        array.remove(404)


def test_references_survive_resize():
    array = DynamicArray()
    payload = {"title": "original"}
    array.append(payload)
    for value in [20, 30, 40, 50]:
        array.append(value)
    payload["title"] = "edited"
    assert array[0] is payload
    assert array[0]["title"] == "edited"
