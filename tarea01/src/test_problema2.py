"""Tests for problema2. Run with: python -m pytest tarea01/src -q"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from problema2 import count_frequencies, print_sorted, split_words


def write_text(tmp_path: Path, content: str) -> Path:
    path = tmp_path / "texto.txt"
    path.write_text(content, encoding="utf-8")
    return path


def test_count_frequencies_counts_repeated_words(tmp_path):
    path = write_text(tmp_path, "El perro de San Roque no tiene rabo. El perro.")

    result = count_frequencies(["perro", "El"], path)

    assert result == {"perro": 2, "el": 2}


def test_count_frequencies_ignores_punctuation(tmp_path):
    path = write_text(tmp_path, "¡Hola, mundo! ¿Hola?")

    result = count_frequencies(["hola", "mundo"], path)

    assert result == {"hola": 2, "mundo": 1}


def test_count_frequencies_ignores_case_and_accents(tmp_path):
    path = write_text(tmp_path, "Programación y PROGRAMACION otra vez.")

    result = count_frequencies(["Programación"], path)

    assert result == {"programacion": 2}


def test_count_frequencies_keeps_words_that_never_appear(tmp_path):
    path = write_text(tmp_path, "solo perro")

    result = count_frequencies(["perro", "gato"], path)

    assert result["gato"] == 0


def test_count_frequencies_only_counts_words_from_the_list(tmp_path):
    path = write_text(tmp_path, "perro perro gato")

    result = count_frequencies(["perro"], path)

    assert result == {"perro": 2}


def test_count_frequencies_with_empty_file(tmp_path):
    path = write_text(tmp_path, "")

    assert count_frequencies(["perro"], path) == {"perro": 0}


def test_count_frequencies_missing_file_raises(tmp_path):
    try:
        count_frequencies(["perro"], tmp_path / "no_existe.txt")
    except FileNotFoundError:
        return
    raise AssertionError("debía lanzar FileNotFoundError")


def test_split_words_cleans_and_lowercases():
    assert list(split_words("¡Hola, mundo!  Adiós.")) == ["hola", "mundo", "adios"]


def test_print_sorted_outputs_words_in_alphabetical_order(tmp_path, capsys):
    path = write_text(tmp_path, "zeta alfa beta")

    print_sorted(count_frequencies(["zeta", "alfa", "beta"], path))

    lines = [line.split()[0] for line in capsys.readouterr().out.splitlines()]
    assert lines == ["alfa", "beta", "zeta"]
