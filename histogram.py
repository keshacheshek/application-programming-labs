import cv2
import matplotlib.pyplot as plt

from numpy import ndarray


def create_histogram(img: ndarray) -> list:
    """
    Создаем список гистограмм для трёх цветовых каналов
    :param img:изображение в виде матрицы пикселей
    :return:список гистограмм
    """
    return [cv2.calcHist([img], [i], None, [256], [0, 256]) for i in range(3)]


def show_histograms_of_channels(histograms: list) -> None:
    """
    Выводим гистограммы трёх цветовых каналов
    :param histograms:список гистограмм для трёх цветов
    """
    colors = ['blue', 'green', 'red']
    for i, col in enumerate(colors):
        plt.plot(histograms[i], label=col, color=col)
    plt.title('Histogram of colors')
    plt.xlabel('Pixel Intensity (0-255)')
    plt.ylabel('Number of Pixels')
    plt.axhline(0, color='black', linewidth=0.5)  # линия по оси x
    plt.axvline(0, color='black', linewidth=0.5)  # линия по оси y
    plt.legend()
    plt.show()
