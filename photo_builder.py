from PIL import Image, ImageDraw, ImageFont
from config import path_main, path_igtv, path_content, path_stat, path_logo

img = Image.open(path_main)


def input_photo(paste_width, paste_high, path, type):
    global img
    photo = Image.open(path)
    w, h = photo.size
    print('scrip')
    print(w)
    print(h)
    x = h
    resized_img = ''
    if 720 > w:
        value = 720 - w
        x += value
        size = (720, int(x))
        resized_img = photo.resize(size)
        if type == 'video':
            input_igtv_logo(30, int(x) - 100, resized_img)
    elif 720 < w:
        x = (h * 720) / w
        if x < 410:
            x = 410
        size = (720, int(x))
        resized_img = photo.resize(size)
        if type == 'video':
            input_igtv_logo(30, int(x) - 70, resized_img)

    img.paste(resized_img, (paste_width, paste_high))
    return h + paste_high


def input_igtv_logo(paste_width, paste_high, image):
    global img
    logo = Image.open(path_igtv)
    size = (40, 40)
    resized_logo = logo.resize(size)
    image.paste(resized_logo, (paste_width, paste_high), resized_logo)


def input_logo(height_of_logo, path):
    # for i in range(20, 100):
    #     for j in range(120, 180):
    #         img.putpixel((i, j), (255, 255, 255))
    logo = Image.open(path)
    size = (57, 57)
    resized_logo = logo.resize(size)
    img.paste(resized_logo, (30, 123), resized_logo)


def input_labels(paste_width, paste_high):
    global img
    photo = Image.open(path_content)
    w, h = photo.size
    size = (720, h)
    resized_img = photo.resize(size)
    img.paste(resized_img, (paste_width, paste_high))


def bright(brightness=0.5):
    global img
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


def print_pixel(range_a, range_b, range_c, range_d, r, g, b):
    for i in range(range_a, range_b):
        for j in range(range_c, range_d):
            img.putpixel((i, j), (r, g, b))


def input_stats():
    global img
    photo = Image.open(path_stat)
    w, h = photo.size
    statistics = photo.resize((720, h))
    img.paste(statistics, (0, 750), statistics)
