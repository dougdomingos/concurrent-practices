from multiprocessing import Manager, Pool
from os import listdir, path


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


def count_words_of_file(file_path: str) -> tuple:
    """Counts the number of words in the file.

    Args:
        file_path (str): The path of the word file
    """

    word_counter = 0

    with open(file_path, "r") as file:
        words = file.readlines()

        for _ in words:
            word_counter += 1
    
    return path.basename(file_path), word_counter


def update_status(results: tuple, stats: dict):
    file_name, word_counter = results

    if word_counter > stats["max_word_count"]:
        stats["max_word_count"] = word_counter
        stats["biggest_file"] = file_name


def get_biggest_file() -> None:
    """Find the biggest file (by word count) within the directory."""

    directory = get_words_directory()

    with Manager() as manager:
        stats = manager.dict({"biggest_file": "", "max_word_count": 0})
        files = [path.join(directory, file) for file in listdir(directory)]

        with Pool(10) as pool:
            for result in pool.imap_unordered(count_words_of_file, files):
                update_status(result, stats)

        print(
            f'Concurrent: The biggest file is {stats["biggest_file"]}, with {stats["max_word_count"]} words.'
        )


if __name__ == "__main__":
    get_biggest_file()
