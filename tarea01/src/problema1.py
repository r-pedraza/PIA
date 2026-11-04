"""Problem 1: process a list of integers.

From an input list of integers, return a new list that:
  1. contains no negative numbers,
  2. contains no repeated values,
  3. is sorted from lowest to highest.

Example:
    [4, -1, 2, 4, 3, -5, 2]  ->  [2, 3, 4]

Deduplication is handled by a set, which cannot hold repeats, and the ordering of
the result is resolved with sorted().
"""

from typing import Iterable, List


def clean_list(numbers: Iterable[int]) -> List[int]:
    """Return the non-negative integers, de-duplicated and sorted.

    Args:
        numbers: iterable of integers (list, tuple or generator).

    Returns:
        Sorted list of integers >= 0 without duplicates. Empty list if no valid
        value remains.

    Raises:
        TypeError: if any element is not an integer.
    """
    # Se materializa una sola vez: si `numbers` fuese un generador, recorrerlo dos
    # veces lo dejaría agotado y el resultado saldría vacío.
    values = list(numbers)

    for value in values:
        # bool is a subclass of int in Python, but it is not accepted as a number here.
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"Se esperaba un entero y llegó {value!r}")

    non_negative = [value for value in values if value >= 0]
    return sorted(set(non_negative))


if __name__ == "__main__":
    samples = [
        [4, -1, 2, 4, 3, -5, 2],
        [],
        [-3, -1],
        [7, 7, 7],
        [0, 5, 5, -2, 1],
    ]
    for sample in samples:
        print(f"{sample} -> {clean_list(sample)}")
