"""Tests for problema1. Run with: python -m pytest tarea01/src -q"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from problema1 import clean_list


def test_clean_list_matches_statement_example():
    assert clean_list([4, -1, 2, 4, 3, -5, 2]) == [2, 3, 4]


def test_clean_list_removes_negatives():
    assert clean_list([-3, -1]) == []


def test_clean_list_removes_duplicates():
    assert clean_list([7, 7, 7]) == [7]


def test_clean_list_accepts_zero_and_keeps_order():
    assert clean_list([5, 0, 5, -2, 1]) == [0, 1, 5]


def test_clean_list_with_empty_input():
    assert clean_list([]) == []


def test_clean_list_does_not_modify_the_input():
    numbers = [3, -1, 3]
    clean_list(numbers)
    assert numbers == [3, -1, 3]


def test_clean_list_accepts_any_iterable():
    assert clean_list(iter([2, 1, 2])) == [1, 2]


def test_clean_list_rejects_non_integers():
    for invalid in ([1, "2"], [1.5], [True]):
        try:
            clean_list(invalid)
        except TypeError:
            continue
        raise AssertionError(f"debía rechazar {invalid!r}")
