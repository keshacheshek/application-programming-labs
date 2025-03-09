import cv2

from numpy import ndarray


def read_image(name_im: str) -> ndarray:
    """
    Переводим изображение в матрицу пикселей
    :param name_im:путь к изображению
    :return:изображение в виде матрицы пикселей
    """
    return cv2.imread(name_im)


def show_image(img: ndarray) -> None:
    """
    Выводим изображения на экран
    :param img:изображение в виде матрицы пикселей
    """
    cv2.imshow('image', img)
    cv2.waitKey(0)


def size(img: ndarray) -> tuple[int,int]:
    """
    Выводим размер изображения
    :param img:изображение в виде матрицы пикселей
    :return:кортеж с параметрами
    """
    height, width, val = img.shape
    return height, width