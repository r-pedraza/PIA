"""Problem 3: set operations on two lists of integers.

The function receives two lists of integers and returns a dictionary with:
  1. the intersection (elements present in both),
  2. the union (every element, without duplicates),
  3. the symmetric difference (elements in one set or the other, but not both).

The statement requires sets to compute them, so every result is derived from
set operations and only turned into a sorted list for a stable, readable output.
"""

from typing import Dict, Iterable, List

SetResults = Dict[str, List[int]]


def _to_set(values: Iterable[int], name: str) -> set:
    """Validate the input and return it as a set.

    Args:
        values: iterable of integers.
        name: parameter name, used to build a helpful error message.

    Returns:
        The values as a set of integers.

    Raises:
        TypeError: if any element is not an integer.
    """
    result = set()
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} debe contener solo enteros, llegó {value!r}")
        result.add(value)
    return result


def compare_sets(first: Iterable[int], second: Iterable[int]) -> SetResults:
    """Return intersection, union and symmetric difference of two lists.

    Args:
        first: first list of integers.
        second: second list of integers.

    Returns:
        Dictionary with keys ``intersection``, ``union`` and
        ``symmetric_difference``. Each value is a sorted list without
        duplicates.

    Raises:
        TypeError: if either input contains a value that is not an integer.
    """
    left = _to_set(first, "La primera lista")
    right = _to_set(second, "La segunda lista")

    return {
        "intersection": sorted(left & right),
        "union": sorted(left | right),
        "symmetric_difference": sorted(left ^ right),
    }


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4], [3, 4, 5, 6]),
        ([1, 2, 2, 3], [2]),
        ([], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
    ]

    for first, second in cases:
        print(f"A = {first}   B = {second}")
        for key, values in compare_sets(first, second).items():
            print(f"  {key:<21} {values}")
        print()
