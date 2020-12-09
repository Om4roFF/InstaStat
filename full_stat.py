from PIL import Image, ImageDraw, ImageFont
from config import path_full_stat

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


def draw_like(height_of_likes, font, like):
    if len(str(like)) == 1:
        width_of_likes = 80
    elif len(str(like)) == 2:
        width_of_likes = 73
    elif len(str(like)) == 3:
        width_of_likes = 64
    elif len(str(like)) == 4:
        width_of_likes = 55
    elif len(str(like)) == 5:
        width_of_likes = 46
    elif len(str(like)) == 6:
        width_of_likes = 37
    elif len(str(like)) == 7:
        width_of_likes = 29
    else:
        width_of_likes = 20
    draw.text((width_of_likes, height_of_likes), str(like), font=font, fill='black')  # put the text on the image


def draw_comment(height_of_comments, font, comment):
    if len(str(comment)) == 1:
        width_of_comments = 260
    elif len(str(comment)) == 2:
        width_of_comments = 253
    elif len(str(comment)) == 3:
        width_of_comments = 244
    elif len(str(comment)) == 4:
        width_of_comments = 235
    elif len(str(comment)) == 5:
        width_of_comments = 226
    elif len(str(comment)) == 6:
        width_of_comments = 217
    elif len(str(comment)) == 7:
        width_of_comments = 209
    else:
        width_of_comments = 200
    draw.text((width_of_comments, height_of_comments), str(comment), font=font, fill='black')


def draw_share(height_of_share, font, share):
    if len(str(share)) == 1:
        width_of_share = 440
    elif len(str(share)) == 2:
        width_of_share = 433
    elif len(str(share)) == 3:
        width_of_share = 424
    elif len(str(share)) == 4:
        width_of_share = 415
    elif len(str(share)) == 5:
        width_of_share = 406
    elif len(str(share)) == 6:
        width_of_share = 400
    elif len(str(share)) == 7:
        width_of_share = 389
    else:
        width_of_share = 383
    draw.text((width_of_share, height_of_share), str(share), font=font, fill='black')


def draw_notes(height_of_notes, font, notes):
    if len(str(notes)) == 1:
        width_of_notes = 622
    elif len(str(notes)) == 2:
        width_of_notes = 613
    elif len(str(notes)) == 3:
        width_of_notes = 604
    elif len(str(notes)) == 4:
        width_of_notes = 595
    elif len(str(notes)) == 5:
        width_of_notes = 588
    elif len(str(notes)) == 6:
        width_of_notes = 582
    elif len(str(notes)) == 7:
        width_of_notes = 571
    else:
        width_of_notes = 565
    draw.text((width_of_notes, height_of_notes), str(notes), font=font, fill='black')


def draw_visits(height_of_visits, font, visits):
    if len(str(visits)) == 1:
        width_of_visits = 168
    elif len(str(visits)) == 2:
        width_of_visits = 160
    elif len(str(visits)) == 3:
        width_of_visits = 150
    elif len(str(visits)) == 4:
        width_of_visits = 140
    elif len(str(visits)) == 5:
        width_of_visits = 125
    elif len(str(visits)) == 6:
        width_of_visits = 110
    elif len(str(visits)) == 7:
        width_of_visits = 100
    else:
        width_of_visits = 90
    draw.text((width_of_visits, height_of_visits), str(visits), font=font, fill='black')


def draw_coverage(height_of_coverage, font, coverage, fill):
    cov = str(coverage)
    if 1000 <= coverage <= 9999:
        cov = cov[0]+' '+cov[1]+cov[2]+cov[3]
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
    draw.text((width, height_of_coverage), str(cov), font=font, fill=fill)


def draw_interaction(height_of_interaction, font, interaction):
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
    inter = str(interest)
    if 1000 <= interest <= 9999:
        inter = inter[0] + ' ' + inter[1] + inter[2] + inter[3]
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
    draw.text((width_of_interest, height_of_interest), str(inter), font=font, fill='black')


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
    draw.text((width, height_of_account), str(account), font=font, fill=fill)


def draw_percent(height_of_percent, font, percent, fill):
    if len(str(percent)) == 1:
        width = 10
    elif len(str(percent)) == 2:
        width = 80
    elif len(str(percent)) == 3:
        width = 75
    else:
        width = 70
    draw.text((width, height_of_percent), str(percent), font=font, fill=fill)


def second_img(interaction, visits, interest, sub, coverage, sh, page, account, percent):
    font1 = ImageFont.truetype("arial.ttf", 32)
    font = ImageFont.truetype("arial.ttf", 28)
    font5 = ImageFont.truetype("arial.ttf", 27)
    font2 = ImageFont.truetype("arial.ttf", 42)
    font3 = ImageFont.truetype("arial.ttf", 52)
    font6 = ImageFont.truetype("arial.ttf", 25)

    clear()
    draw_interaction(310, font3, interaction)
    draw_visits_full(484, font1, visits)
    draw_interest(700, font3, interest)
    draw_coverage(998, font1, sub, 'black')
    draw_coverage(1080, font1, coverage, 'black')
    draw_coverage(918, font1, sh, 'black')
    draw_coverage(1135, font5, page, 'gray')
    draw_account(818, font, account, 'gray')
    draw_percent(822, font6, percent, 'gray')
    img.save('media/ws2.jpg')
    img.show()
