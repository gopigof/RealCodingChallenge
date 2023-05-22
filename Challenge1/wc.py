import argparse
import fileinput


FILE_CONTENT_STDIN_FLAG = "#.#."


def get_byte_count(file_content: str) -> int:
    """
    Get the number of bytes in the given file
    :param file_content: path
    :return: int
    """
    return len(file_content.encode("utf-8"))


def get_line_count(file_content: str) -> int:
    """
    Get the number of lines in the given file
    :param file_content: path
    :return: int
    """
    return file_content.count("\n")


def get_word_count(file_content: str) -> int:
    """
    Get the number of words present in the given file
    :param file_content: path
    :return: int
    """
    return len(file_content.split())


def get_character_count(file_content: str) -> int:
    """

    :param file_content:
    :return:
    """
    return sum(len(word) for word in file_content.split())


def main(file: str, flag_c: bool = False, flag_l: bool = False, flag_w: bool = False, flag_m: bool = False) -> None:
    try:
        with fileinput.input(file, encoding="utf-8") as buffer:
            file_content: str = "".join((line for line in buffer))
    except FileNotFoundError:
        print(f"File path: {file}: doesn't exist ")
        return

    # print(file_content)
    counts = []
    # Default case, when no flags are provided
    if not any((flag_c, flag_l, flag_w)) and not flag_m:
        flag_c = flag_l = flag_w = True

    if flag_l:
        counts.append(get_line_count(file_content))
    if flag_w:
        counts.append(get_word_count(file_content))
    if flag_c:
        counts.append(get_byte_count(file_content))
    if flag_m:
        counts.append(get_character_count(file_content))

    print(' '.join(map(str, counts)), end=" ")
    if file != FILE_CONTENT_STDIN_FLAG:
        print(file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", action="store_true", dest="flag_c", help="Print the byte counts")
    parser.add_argument("-l", action="store_true", dest="flag_l", help="Print the line counts")
    parser.add_argument("-w", action="store_true", dest="flag_w", help="Print the word counts")
    parser.add_argument("-m", action="store_true", dest="flag_m", help="Print the character counts")
    parser.add_argument("file", action="store", nargs="?", default=None, help="Path of file")
    args = parser.parse_args()

    main(args.file, args.flag_c, args.flag_l, args.flag_w, args.flag_m)
