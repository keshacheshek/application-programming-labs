import argparse #python lab-3.py image.jpg 42

from img_read import read_image, show_image, size
from histogram import create_histogram, show_histograms_of_channels
from rotate_img import rotate_image


def arg_parse() -> tuple[str, int]:
    """
    Парсинг аргументов командной строки
    :return: кортеж из названия файла для поворота и градуса
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('name_file', type=str, help='Name of the image file.')
    parser.add_argument('angle', type=int, help='Rotation angle in degrees.')
    args = parser.parse_args()
    return args.name_file, args.angle


def main():
    name_file, angle = arg_parse()
    try:
        img = read_image(name_file)
        show_image(img)
        size_img = size(img)
        print(f"Image size: {size_img}")
        histogram_of_channels = create_histogram(img)
        show_histograms_of_channels(histogram_of_channels)
        rotated_im = rotate_image(img, angle)
        show_image(rotated_im)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()