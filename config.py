import logging


path_main = 'static/builder/main_page.jpg'
path_igtv = 'static/builder/igtv-logo-circle-black-and-white.png'
path_video = 'static/builder/video.png'
path_content = 'static/builder/main_pagg.jpg'
path_stat = 'static/builder/SL.png'
path_full_stat = 'static/builder/full.jpg'
path_carousel = 'static/builder/шаблон.png'


def log():
    logger = logging.getLogger('InstaStat')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('instaStat.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

