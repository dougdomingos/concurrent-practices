from os import listdir, path
from multiprocessing import Lock, Manager, Process


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


def count_words_of_file(file_path: str, lock, stats: dict) -> None:
    """Counts the number of words in the file.

    Args:
        file_path (str): The path of the word file
    """

    word_counter = 0

    with open(file_path, "r") as file:
        words = file.readlines()

        for _ in words:
            word_counter += 1

    with lock:
        if word_counter > stats["max_word_count"]:
            stats["max_word_count"] = word_counter
            stats["biggest_file"] = path.basename(file_path)


def get_biggest_file() -> None:
    """Find the biggest file (by word count) within the directory."""

    directory = get_words_directory()

    with Manager() as manager:
        stats = manager.dict({"biggest_file": "", "max_word_count": 0})
        lock = Lock()
        processes = []

        for file in listdir(directory):
            file_path = path.join(directory, file)
            new_process = Process(target=count_words_of_file, args=(file_path, lock, stats))
            processes.append(new_process)
            new_process.start()

        for process in processes:
            process.join()

        print(
            f'Concurrent: The biggest file is {stats["biggest_file"]}, with {stats["max_word_count"]} words.'
        )


if __name__ == "__main__":
    get_biggest_file()
