from PIL import Image, ImageDraw, ImageFont
from photo_builder import img


draw = ImageDraw.Draw(img)


def draw_like(height_of_likes, font, like):
    for i in range(720):
        for j in range(970, 1100):
            img.putpixel((i, j), (255, 255, 255))
    like = separation(str(like))
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
    comment = separation(str(comment))
    if len(str(comment)) == 1:
        width_of_comments = 265
    elif len(str(comment)) == 2:
        width_of_comments = 255
    elif len(str(comment)) == 3:
        width_of_comments = 244
    elif len(str(comment)) == 4:
        width_of_comments = 238
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
    share = separation(str(share))
    if len(str(share)) == 1:
        width_of_share = 445
    elif len(str(share)) == 2:
        width_of_share = 435
    elif len(str(share)) == 3:
        width_of_share = 430
    elif len(str(share)) == 4:
        width_of_share = 420
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
    notes = separation(str(notes))
    if len(str(notes)) == 1:
        width_of_notes = 625
    elif len(str(notes)) == 2:
        width_of_notes = 615
    elif len(str(notes)) == 3:
        width_of_notes = 604
    elif len(str(notes)) == 4:
        width_of_notes = 597
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
    for i in range(720):
        for j in range(1100, 1160):
            img.putpixel((i, j), (255, 255, 255))
    visits = separation(str(visits))
    if len(str(visits)) == 1:
        width_of_visits = 170
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


def draw_coverage(height_of_coverage, font, coverage):
    coverage = separation(str(coverage))
    if len(str(coverage)) == 1:
        width_of_coverage = 527
    elif len(str(coverage)) == 2:
        width_of_coverage = 520
    elif len(str(coverage)) == 3:
        width_of_coverage = 505
    elif len(str(coverage)) == 4:
        width_of_coverage = 495
    elif len(str(coverage)) == 5:
        width_of_coverage = 490
    elif len(str(coverage)) == 6:
        width_of_coverage = 475
    elif len(str(coverage)) == 7:
        width_of_coverage = 465
    else:
        width_of_coverage = 455
    draw.text((width_of_coverage, height_of_coverage), str(coverage), font=font, fill='black')


def separation(number):
    number = str(number)[::-1]
    l = [number[i:i + 3] for i in range(0, len(number), 3)]
    l.reverse()
    s = ' '.join([number[i:i+3] for i in range(0, len(number), 3)])
    s = s[::-1]
    return s


def draw_name(height_of_name, font, name, fill):
    for i in range(100, 350):
        for j in range(130, 180):
            img.putpixel((i, j), (255, 255, 255))
    width_of_name = 105
    draw.text((width_of_name, height_of_name), str(name), font=font, fill=fill)


