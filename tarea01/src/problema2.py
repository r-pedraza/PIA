"""Problem 2: word frequency of a word list inside a text file.

The function receives a list of words and the path to a text file, and returns a
dictionary {word: frequency}. Before counting:

  1. punctuation signs are removed,
  2. everything is lowercased.

The result is printed sorted alphabetically by word.

Only the words given in the input list are counted; the rest of the text is
ignored, which is the literal reading of the statement.
"""

import string
import unicodedata
from pathlib import Path
from typing import Dict, Iterable, Iterator, Union

PathLike = Union[str, Path]


def _normalize(word: str) -> str:
    """Return the word lowercased and without accents.

    Striping accents makes 'Programación' and 'programacion' count as the same
    word, which is what a reader expects.
    """
    decomposed = unicodedata.normalize("NFKD", word)
    without_accents = "".join(char for char in decomposed if not unicodedata.combining(char))
    return without_accents.lower()


def _clean_word(word: str) -> str:
    """Remove surrounding punctuation and normalize the rest."""
    without_punctuation = word.strip(string.punctuation + "¿¡«»“”‘’")
    return _normalize(without_punctuation)


def split_words(text: str) -> Iterator[str]:
    """Yield the words of a text, cleaned and lowercased."""
    for raw_word in text.split():
        clean = _clean_word(raw_word)
        if clean:
            yield clean


def count_frequencies(words: Iterable[str], path: PathLike) -> Dict[str, int]:
    """Count how many times each word appears in the file.

    Args:
        words: words to look for. They are normalized the same way as the text,
            so uppercase or accented input is accepted.
        path: path to the text file (UTF-8).

    Returns:
        Dictionary {normalized_word: frequency} containing every word from the
        input list as a key, even those that never appear.

    Raises:
        FileNotFoundError: if the path does not exist or is not a file.
    """
    wanted = {_normalize(word) for word in words}
    frequencies = {word: 0 for word in wanted}

    text = Path(path).read_text(encoding="utf-8")
    for found in split_words(text):
        if found in frequencies:
            frequencies[found] += 1

    return frequencies


def print_sorted(frequencies: Dict[str, int]) -> None:
    """Print the dictionary sorted alphabetically by word."""
    width = max((len(word) for word in frequencies), default=0)
    for word in sorted(frequencies):
        print(f"{word:<{width}}  {frequencies[word]}")


if __name__ == "__main__":
    # Sample file created next to this script if it is not there yet.
    sample_path = Path(__file__).with_name("sample_text.txt")
    if not sample_path.exists():
        sample_path.write_text(
            "El perro de San Roque no tiene rabo. "
            "¡El perro de Ramón tampoco tiene rabo! "
            "¿Quién le ha cortado el rabo al perro?",
            encoding="utf-8",
        )

    word_list = ["perro", "rabo", "Rabo", "Roque", "gato", "EL"]
    result = count_frequencies(word_list, sample_path)

    print(f"Fichero: {sample_path.name}")
    print_sorted(result)
