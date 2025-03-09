import os

from icrawler.builtin import GoogleImageCrawler

def download_img(keyword: str, num_img = 50, save_dir: str="image",) -> None:
    """
    Скачиваем изображения в нужную папку
    :param save_dir: папка в которую сохраняются изображения
    :param num_img: количество изображений
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    google_crawler = GoogleImageCrawler(storage={'root_dir': save_dir})
    google_crawler.crawl(keyword = keyword, max_num = num_img)