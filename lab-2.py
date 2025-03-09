import argparse #python lab-2.py monkey image annot.csv

from iterator import ImageIterator
from download_img import download_img
from annotation import create_annotation


def print_list(p_list: ImageIterator) -> None:
    """
    Выводим в консоль содержимое папки либо файла
    :param p_list: Итератор файла или папки
    """
    for row in p_list:
        print(row)

def arg_parser() -> tuple[str, str, str]:
    """
    Парсинг аргументов командной строки
    :return: кортеж из ключевого слова для поиска, пути к папке для сохранения изображений и пути к файлу аннотации
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str, help='the search keyword')
    parser.add_argument('--annotation_path', type=str, default='annot.csv', help='the path to the annotation file(absolute/relative)')
    parser.add_argument('--save_folder', type=str, default='images', help='the path to the folder to save(absolute/relative)')
    args = parser.parse_args()
    return args.keyword, args.save_folder, args.annotation_path


def main():
    try:
        keyword, annot_path, save_folder = arg_parser()
        download_img(keyword, 10, save_folder)
        create_annotation(save_folder, annot_path)

        print("Annotation iterator:")
        print_list(ImageIterator(annot_path))

        print("Image directory iterator:")
        print_list(ImageIterator(save_folder))
    except Exception as e:
        print(f"Error: {e}")
        return

if __name__ == '__main__':
    main()