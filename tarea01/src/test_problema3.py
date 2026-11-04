"""Tests for problema3. Run with: python -m pytest tarea01/src -q"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from problema3 import compare_sets


def test_compare_sets_returns_all_three_operations():
    result = compare_sets([1, 2, 3, 4], [3, 4, 5, 6])

    assert result["intersection"] == [3, 4]
    assert result["union"] == [1, 2, 3, 4, 5, 6]
    assert result["symmetric_difference"] == [1, 2, 5, 6]


def test_compare_sets_handles_duplicates():
    result = compare_sets([1, 2, 2, 3], [2, 2])

    assert result["intersection"] == [2]
    assert result["union"] == [1, 2, 3]


def test_compare_sets_with_empty_list():
    result = compare_sets([], [1, 2])

    assert result["intersection"] == []
    assert result["union"] == [1, 2]
    assert result["symmetric_difference"] == [1, 2]


def test_compare_sets_with_identical_lists():
    result = compare_sets([1, 2, 3], [3, 2, 1])

    assert result["intersection"] == [1, 2, 3]
    assert result["symmetric_difference"] == []


def test_compare_sets_with_disjoint_lists():
    result = compare_sets([1, 2], [3, 4])

    assert result["intersection"] == []
    assert result["union"] == [1, 2, 3, 4]


def test_compare_sets_does_not_modify_the_input():
    first, second = [1, 2], [2, 3]
    compare_sets(first, second)

    assert first == [1, 2]
    assert second == [2, 3]


def test_compare_sets_rejects_non_integers():
    try:
        compare_sets([1, "dos"], [1])
    except TypeError:
        return
    raise AssertionError("debía rechazar valores que no son enteros")
