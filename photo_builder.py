import datetime
import re
import time

import requests
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from config import path_igtv, path_content, path_stat, path_video, path_carousel
from config import log
logger = log()


def input_photo(img, paste_width, paste_high, url, type, carousel_count, video_duration):
    try:
        logger.info('input_photo')
        myfile = requests.get(url)
        open(f'static/media/1.png', 'wb').write(myfile.content)
        time.sleep(2)
        photo = Image.open('static/media/1.png').convert("RGBA")
        w, h = photo.size
        print(w, h)
        y = h
        resized_img = ''
        if 720 >= w:
            value = 720 - w
            y += value
            size = (720, int(y))
            resized_img = photo.resize(size)
            resized_img = media_type_small(type, y, resized_img, video_duration, carousel_count)
        elif 720 < w:
            y = (h * 720) / w
            if y < 410:
                y = 410
            size = (720, int(y))
            resized_img = photo.resize(size)
            resized_img = media_type_large(type, y, resized_img, video_duration, carousel_count)
        x, y = resized_img.size
        img.paste(resized_img, (paste_width, paste_high))
        return y + paste_high
    except Exception as e:
        logger.info(e)


def media_type_small(type_of_media, y, image, video_duration, count):
    if type_of_media == 'video' or type_of_media == 'igtv':
        input_igtv_logo(30, int(y) - 100, image)
        # input_video_logo(700, 300, image)
        if video_duration != '':
            draw_video_duration(video_duration, image)
    elif type_of_media == 'carousel':
        if count != '':
            draw_carousel(count, image)
    return image


def media_type_large(type_of_media, y, image, video_duration, count):
    if type_of_media == 'video' or type_of_media == 'igtv':
        input_igtv_logo(30, int(y) - 70, image)
        # input_video_logo(670, 35, image)
        if video_duration != '':
            draw_video_duration(video_duration, image)
    elif type_of_media == 'carousel':
        if count != '':
            draw_carousel(count, image)
    return image


def input_igtv_logo(paste_width, paste_high, image):
    logo = Image.open(path_igtv)
    size = (40, 40)
    resized_logo = logo.resize(size)
    image.paste(resized_logo, (paste_width, paste_high), resized_logo)


def input_video_logo(paste_width, paste_high, image):
    logo = Image.open(path_video)
    size = (70, 70)
    resized_logo = logo.resize(size)
    image.paste(resized_logo, (paste_width, paste_high), resized_logo)


def input_logo(img, path):
    for i in range(25, 95):
        for j in range(120, 185):
            img.putpixel((i, j), (255, 255, 255))
    myfile = requests.get(path)
    open(f'static/media/logo.png', 'wb').write(myfile.content)
    time.sleep(2)
    logo = Image.open('static/media/logo.png').convert("RGBA")
    size = (57, 57)
    resized_logo = logo.resize(size)
    im = crop(resized_logo, size)
    im.putalpha(prepare_mask(size, 4))
    img.paste(im, (30, 123), im)


def input_labels(img, paste_width, paste_high):
    photo = Image.open(path_content)
    w, h = photo.size
    size = (720, h)
    resized_img = photo.resize(size)
    img.paste(resized_img, (paste_width, paste_high))


def bright(img, brightness):
    source = img
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            red = int(r * brightness)
            red = min(255, max(0, red))
            green = int(g * brightness)
            green = min(255, max(0, green))
            blue = int(b * brightness)
            blue = min(255, max(0, blue))
            img.putpixel((x, y), (red, green, blue))


def input_stats(img):
    photo = Image.open(path_stat)
    w, h = photo.size
    statistics = photo.resize((720, h))
    img.paste(statistics, (0, 750), statistics)


def draw_video_duration(video_duration, image):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 23)
    minutes = str(datetime.timedelta(seconds=video_duration))
    minutes = str(minutes)[3:7]
    draw.text((645, 30), minutes, font=font, fill='white')


def draw_carousel(count, image):
    photo = Image.open(path_carousel)
    font = ImageFont.truetype("arial.ttf", 24)
    x, y = photo.size
    print(x, y)
    resized_img = photo.resize((65, 40))
    resized_img = ReduceOpacity(resized_img, 0.8)
    draw = ImageDraw.Draw(resized_img)
    draw.text((14, 6), '1/'+str(count), font=font, fill='white')
    image.paste(resized_img, (645, 30), resized_img)


def prepare_mask(size, antialias=2):
    mask = Image.new('L', (size[0] * antialias, size[1] * antialias), 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + mask.size, fill=255)
    return mask.resize(size, Image.ANTIALIAS)


def crop(im, s):
    w, h = im.size
    k = w / s[0] - h / s[1]
    if k > 0:
        im = im.crop(((w - h) / 2, 0, (w + h) / 2, h))
    elif k < 0:
        im = im.crop((0, (h - w) / 2, w, (h + w) / 2))
    return im.resize(s, Image.ANTIALIAS)


def ReduceOpacity(im, opacity):
    assert 0 <= opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im