from os import listdir, path

biggest_file = ""
max_word_count = 0


def get_words_directory() -> str:
    """Get the absolute path of the directory that contains the word files.

    Raises:
        FileNotFoundError: If the directory is not found

    Returns:
        str: The path of the directory
    """

    dir_path = path.join(path.dirname(path.abspath(__file__)), "files")

    if not path.exists(dir_path):
        raise FileNotFoundError(
            f'Directory {dir_path} does not exists! Have you run "setup.py"?'
        )

    return dir_path


def count_words_of_file(file_path: str) -> int:
    """Counts the number of words in the file.

    Args:
        file_path (str): The path of the word file

    Returns:
        int: The number of words within the file
    """

    word_counter = 0

    with open(file_path, "r") as file:
        words = file.readlines()

        for _ in words:
            word_counter += 1

    return word_counter


def update_stats_if_greater(file_name: str, word_count: int) -> None:
    """Updates the global counter and file path if the current file has more words.

    Args:
        file_name (str): The name of the current file
        word_count (int): The number of words within the current file
    """

    global max_word_count
    global biggest_file

    if word_count > max_word_count:
        max_word_count = word_count
        biggest_file = file_name


def get_biggest_file() -> None:
    """Find the biggest file (by word count) within the directory."""

    directory = get_words_directory()

    for file in sorted(listdir(directory)):
        file_path = path.join(directory, file)
        update_stats_if_greater(file, count_words_of_file(file_path))


if __name__ == "__main__":
    get_biggest_file()
    print(f"Serial: The biggest file is {biggest_file}, with {max_word_count} words.")
