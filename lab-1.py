import argparse
import re


def get_arg_parser() -> str:
    """
    Парсинг аргументов командной строки
    :return: название читаемого файла
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str, help='name of file')
    args = parser.parse_args()
    return args.file_name


def read_file(name_file: str) -> str:
    """
    Читаем весь файл в строку
    :param name_file: имя читаемого файла
    :return: текст в строке
    """

    with open(name_file, 'r', encoding='utf-8') as file:
        return file.read()


def split(text: str) -> list[str]:
    """

    :param text:
    :return:
    """
    pattern = r'\d+\)\s*'
    return re.split(pattern, text)


def search(s_list: list[str]) -> list[str]:
    """

    :param s_list:
    :return:
    """
    pattern = r'Фамилия: Иванов[а]?'
    summary_list = list()
    for  checked in s_list:
        if re.search(pattern, checked):
            summary_list.append(checked)
    return summary_list


def print_list(s_list: list[str]) -> None:
    """

    :param s_list:
    :return:
    """
    for check in s_list:
        print(check)


def main():
    file_name = get_arg_parser()
    try:
        text = read_file(file_name)
    except Exception as e:
        print(f"Error: {e}")
        return
    text_list = split(text)
    true_list = search(text_list)
    print_list(true_list)


if __name__ == "__main__":
    main()