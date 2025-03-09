import csv
import os


def get_relative_path(absolute_path: str) -> str:
    """
    Получаем относительный путь до изображений
    :param absolute_path: полный путь к изображениям
    :return: путь к файлу относительно исполняемого файла
    """
    return os.path.relpath(absolute_path)


def create_annotation(files_folder: str, annotation_path: str="annotation.csv") -> None:
    """
    Создаем аннотацию вида [имя файла, абсолютный путь, относительный путь]
    :param annotation_path: путь к файлу аннотации, в который будем все записывать
    :param files_folder: путь к папке, содержащей файлы для аннотации
    """
    file_list = os.listdir(files_folder)
    data = [["Image", "Absolute path", "Relative path"]]
    for file in file_list:
        file_abspath = os.path.abspath(os.path.join(files_folder, file))
        data.append([file, file_abspath, get_relative_path(file_abspath)])
    os.makedirs(os.path.abspath(os.path.dirname(annotation_path)), exist_ok=True)
    with open(annotation_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)