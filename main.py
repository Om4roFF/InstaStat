import time
import os
import tempfile
from flask import Flask, send_file, send_from_directory, request
from PIL import ImageFont
import json
from full_stat import second_img
from photo_builder import bright, input_photo, input_labels, input_stats, input_logo
from draw_image import draw_name, draw_like, draw_comment, draw_share, draw_notes, draw_visits, draw_coverage
from photo_builder import img

font1 = ImageFont.truetype('FontsFree-Net-arial-bold.ttf', 28)
font2 = ImageFont.truetype("arial.ttf", 42)
font3 = ImageFont.truetype("arial.ttf", 32)

app = Flask(__name__)


@app.route('/get_image1', methods=['POST', 'GET'])
def home():
    json_string = request.stream.read().decode('utf-8').strip()
    a = json.loads(json_string.strip())
    url = a['url']
    type = a['type']
    likes = a['likes']
    comments = a['comments']
    shares = a['shares']
    notes = a['notes']
    visits = a['visits']
    coverage = a['coverage']
    name = a['name']
    logo = a['logo']
    main_img(url, type, likes, comments, shares, notes, visits, coverage, name, logo)
    time.sleep(6)
    return send_file(filename_or_fp='media/ws1.jpg', mimetype='image/jpg')


def main_img(url, type, likes, comments, shares, notes, visits, coverages, name, logo):
    y = input_photo(0, 200, url, type)
    input_labels(0, y)
    draw_name(140, font1, name, 'black')
    input_logo(80, logo)
    bright(0.7)
    input_stats()
    height_of_content = 980
    height_of_vc = 1105
    draw_like(height_of_content, font3, likes)
    draw_comment(height_of_content, font3, comments)
    draw_share(height_of_content, font3, shares)
    draw_notes(height_of_content, font3, notes)
    draw_visits(height_of_vc, font2, visits)
    draw_coverage(height_of_vc, font2, coverages)
    w, h = img.size
    print(w, h)
    tf = tempfile.NamedTemporaryFile()
    file_name = tf.name
    img.save('media/ws1.jpg')


@app.route('/get_image2', methods=['GET', 'POST'])
def second():
    json_string = request.stream.read().decode('utf-8').strip()
    a = json.loads(json_string.strip())
    interaction = a['interaction']
    visits = a['visits']
    interest = a['interest']
    sub = a['subscribers']
    coverage = a['coverage']
    screenings = a['screenings']
    page = a['pages']
    account = a['account']
    second_img(interaction, visits, interest, sub, coverage, screenings, page, account, '31%')
    time.sleep(6)
    return send_file(filename_or_fp='media/ws2.jpg', mimetype='image/jpg')


@app.route('/nurs', methods=['GET'])
def hello():
    return 'hello!'


if __name__ == '__main__':
    app.run(debug=False)


# second_img(31,62,13,2,1,2,1,'31','31')
# main_img('https://media.wired.com/photos/598e35fb99d76447c4eb1f28/master/pass/phonepicutres-TA.jpg', 'video.png',
#          1231, 324, 655, 777, 81, 38, 'facebook',
#          'https://i.pinimg.com/originals/72/a3/d9/72a3d9408d41335f39e9f014dc35cf44.jpg')
