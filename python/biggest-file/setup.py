from sys import argv
from os import path, makedirs
from random import sample, randint
from typing import List

NUM_FILES = 100
MAX_WORDS_PER_FILE = 10_000


def load_custom_parameters() -> None:
    """Loads custom number of files and words if specified."""

    global NUM_FILES
    global MAX_WORDS_PER_FILE

    if len(argv) == 3:
        NUM_FILES = int(argv[1])
        MAX_WORDS_PER_FILE = int(argv[2])


def load_wordlist() -> List[str]:
    """Extract the wordlist from the dictionary file.

    Returns:
        List[str]: A list of words
    """

    WORDFILE_PATH = f"{path.dirname(path.abspath(__file__))}/wordlist"

    with open(WORDFILE_PATH, "r") as dict_file:
        wordlist = dict_file.readlines()

    return wordlist


def get_random_words(wordlist: List[str]) -> List[str]:
    """Get a sample of random words from a word list.

    Args:
        word_list (List[str]): The provided word list for sampling

    Returns:
        List[str]: The list of random words
    """

    return sample(wordlist, randint(1, MAX_WORDS_PER_FILE))


def create_text_file(file_path: str, content: List[str]) -> None:
    """Create a file at the specified path with its contents.

    Args:
        file_path (str):     The location in which the file will be created
        content (List[str]): The contents of the file
    """

    with open(file_path, "w") as text_file:
        text_file.writelines(content)


def create_files(target_dir: str) -> None:
    """Create a predefined number of text files at the specified directory.

    Args:
        target_dir (str): The directory where the files will be created
    """

    WORDLIST = load_wordlist()

    for i in range(1, NUM_FILES + 1):
        create_text_file(f"{target_dir}/file_{i:03}.txt", get_random_words(WORDLIST))


def create_file_directory(dir_name: str = "files") -> str:
    """Create the directory that will store the text files.

    Args:
        dir_name (str): The name of the directory

    Returns:
        str: The path of the directory
    """

    current_dir = path.dirname(path.abspath(__file__))
    files_dir = path.join(current_dir, dir_name)
    makedirs(files_dir, exist_ok=True)

    return files_dir


if __name__ == "__main__":
    load_custom_parameters()
    files_dir = create_file_directory()
    create_files(files_dir)
    print(f"Created {NUM_FILES} files at {files_dir}")
