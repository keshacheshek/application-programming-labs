import csv
import os


class ImageIterator:
    def __init__(self, path_file_dir: str) -> None:
        """
        конструктор
        :param path_file_dir: путь к файлу или папке
        """
        self.source = path_file_dir
        self.image_paths = []
        self.index = 0

        # Если source - это файл-аннотация
        if os.path.isfile(path_file_dir):
            with open(path_file_dir, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Пропускаем заголовок
                for row in reader:
                    self.image_paths.append(row[1])  # Предполагаем, что абсолютный путь к изображению во втором столбце
        # Если source - это папка
        elif os.path.isdir(path_file_dir):
            self.image_paths = [os.path.join(path_file_dir, file) for file in os.listdir(path_file_dir)]


    def __iter__(self) -> 'ImageIterator':
        """
        :return: возврат текущего объекта класса
        """
        return self


    def __next__(self) -> str:
        """
        Метод прохода по всем элементам массива класса через индекс и вывода их на экран
        :return: путь к текущему изображению
        """
        if self.index < len(self.image_paths):
            image_path = self.image_paths[self.index]
            self.index += 1
            return image_path
        else:
            raise StopIteration