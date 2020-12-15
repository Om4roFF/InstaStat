import datetime
from PIL import Image, ImageDraw, ImageFont
from config import path_full_stat
from draw_image import separation
img = Image.open(path_full_stat)


def clear():
    for i in range(200, 600):
        for j in range(310, 370):
            img.putpixel((i, j), (255, 255, 255))

    for i in range(300, 700):
        for j in range(450, 550):
            img.putpixel((i, j), (255, 255, 255))

    for i in range(150, 600):
        for j in range(700, 780):
            img.putpixel((i, j), (255, 255, 255))
    #
    for i in range(450, 710):
        for j in range(900, 960):
            img.putpixel((i, j), (255, 255, 255))

    for i in range(450, 710):
        for j in range(980, 1050):
            img.putpixel((i, j), (255, 255, 255))

    for i in range(450, 710):
        for j in range(1070, 1120):
            img.putpixel((i, j), (255, 255, 255))

    for i in range(450, 710):
        for j in range(1120, 1173):
            img.putpixel((i, j), (255, 255, 255))

    for i in range(435, 710):
        for j in range(820, 860):
            img.putpixel((i, j), (255, 255, 255))

    for i in range(0, 130):
        for j in range(820, 860):
            img.putpixel((i, j), (255, 255, 255))


draw = ImageDraw.Draw(img)


def draw_coverage(height_of_coverage, font, coverage, fill):
    if coverage == 'Недоступно':
        width = 530
    else:
        coverage = separation(int(coverage))
        if len(str(coverage)) == 1:
            width = 640
        elif len(str(coverage)) == 2:
            width = 630
        elif len(str(coverage)) == 3:
            width = 620
        elif len(str(coverage)) == 4:
            width = 610
        elif len(str(coverage)) == 5:
            width = 600
        elif len(str(coverage)) == 6:
            width = 590
        elif len(str(coverage)) == 7:
            width = 580
        else:
            width = 570

    draw.text((width, height_of_coverage), str(coverage), font=font, fill=fill)


def draw_interaction(height_of_interaction, font, interaction):
    if interaction == 'Недоступно':
        width_of_interaction = 240
        font = ImageFont.truetype("arial.ttf", 48)
    else:
        interaction = separation(int(interaction))
        if len(str(interaction)) == 1:
            width_of_interaction = 345
        elif len(str(interaction)) == 2:
            width_of_interaction = 335
        elif len(str(interaction)) == 3:
            width_of_interaction = 325
        elif len(str(interaction)) == 4:
            width_of_interaction = 315
        elif len(str(interaction)) == 5:
            width_of_interaction = 305
        elif len(str(interaction)) == 6:
            width_of_interaction = 295
        elif len(str(interaction)) == 7:
            width_of_interaction = 285
        else:
            width_of_interaction = 275
    draw.text((width_of_interaction, height_of_interaction), str(interaction), font=font, fill='black')


def draw_visits_full(height_of_visits, font, visits):
    if visits == 'Недоступно':
        width_of_visits = 530
    else:
        visits = separation(int(visits))
        if len(str(visits)) == 1:
            width_of_visits = 664
        elif len(str(visits)) == 2:
            width_of_visits = 640
        elif len(str(visits)) == 3:
            width_of_visits = 650
        elif len(str(visits)) == 4:
            width_of_visits = 630
        elif len(str(visits)) == 5:
            width_of_visits = 620
        elif len(str(visits)) == 6:
            width_of_visits = 605
        elif len(str(visits)) == 7:
            width_of_visits = 585
        else:
            width_of_visits = 570
    draw.text((width_of_visits, height_of_visits), str(visits), font=font, fill='black')


def draw_interest(height_of_interest, font, interest):
    if interest == 'Недоступно':
        width_of_interest = 240
        font = ImageFont.truetype("arial.ttf", 48)
    else:
        interest = separation(interest)
        if len(str(interest)) == 1:
            width_of_interest = 335
        elif len(str(interest)) == 2:
            width_of_interest = 325
        elif len(str(interest)) == 3:
            width_of_interest = 315
        elif len(str(interest)) == 4:
            width_of_interest = 295
        elif len(str(interest)) == 5:
            width_of_interest = 295
        elif len(str(interest)) == 6:
            width_of_interest = 285
        elif len(str(interest)) == 7:
            width_of_interest = 275
        else:
            width_of_interest = 265
    draw.text((width_of_interest, height_of_interest), str(interest), font=font, fill='black')


def draw_account(height_of_account, font, account, fill):
    if len(str(account)) == 1:
        width = 440
    elif len(str(account)) == 2:
        width = 440
    elif len(str(account)) == 3:
        width = 440
    elif len(str(account)) == 4:
        width = 440
    elif len(str(account)) == 5:
        width = 440
    elif len(str(account)) == 6:
        width = 440
    elif len(str(account)) == 7:
        width = 440
    else:
        width = 440
    draw.text((width, height_of_account), str(account), font=font, fill=(155, 155, 155))


def draw_percent(height_of_percent, font, percent, fill):
    if len(str(percent)) == 1:
        width = 10
    elif len(str(percent)) == 2:
        width = 88
    elif len(str(percent)) == 3:
        width = 83
    else:
        width = 80
    draw.text((width, height_of_percent), str(percent), font=font, fill=(155, 155, 155))


def second_img(profile_view, reach, sub, impressions, page, account, reach_not_follower=None):
    font1 = ImageFont.truetype("arial.ttf", 32)
    font = ImageFont.truetype("arial.ttf", 28)
    font5 = ImageFont.truetype("arial.ttf", 27)
    font2 = ImageFont.truetype("arial.ttf", 42)
    font3 = ImageFont.truetype("arial.ttf", 52)
    font6 = ImageFont.truetype("arial.ttf", 24)
    if reach_not_follower is not None and reach is not None:
        percent = (reach_not_follower*100)/reach
        percent = int(percent)
    else:
        percent = 5
    percent = str(percent) + '%'
    clear()
    draw_interaction(310, font3, profile_view)
    draw_visits_full(484, font1, profile_view)
    draw_interest(700, font3, reach)
    draw_coverage(998, font1, reach, 'black')
    draw_coverage(1080, font1, sub, 'black')
    draw_coverage(918, font1, impressions, 'black')
    draw_coverage(1135, font5, page, 'gray')
    draw_account(818, font, account, 'gray')
    draw_percent(822, font6, percent, 'gray')
    now = datetime.datetime.now()
    file_name = now.strftime('%d%m%y_%H%M%S_') + 'page2_' + account + '.jpg'
    img.save(f'static/media/{file_name}')
    return file_name
