import datetime
import time
import os
import tempfile
from flask import Flask, send_file, send_from_directory, request, jsonify, url_for, redirect
from PIL import ImageFont
import json

from config import path_main
from full_stat import second_img
from photo_builder import bright, input_photo, input_labels, input_stats, input_logo
from draw_image import draw_name, draw_like, draw_comment, draw_share, draw_notes, draw_visits, draw_coverage
from PIL import Image

font1 = ImageFont.truetype('FontsFree-Net-arial-bold.ttf', 28)
font2 = ImageFont.truetype("arial.ttf", 42)
font3 = ImageFont.truetype("arial.ttf", 32)
UPLOAD_FOLDER = '/home/user/InstaStat/media'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/get_image', methods=['POST'])
def home():
    json_string = request.stream.read().decode('utf-8').strip()
    a = json.loads(json_string.strip())
    print(a)
    carousel_count = ''
    video_duration = ''
    if 'carousel_count' in a:
        carousel_count = a['carousel_count']
    if 'video_duration' in a:
        video_duration = a['video_duration']

    for key, value in a.items():
        if value is None:
            a[key] = 'Недоступно'
    url = a['url_poster']
    type = a['media_type']
    likes = a['likes']
    comments = a['comments']
    shares = a['shares']
    notes = a['saves']
    profile_view = a['profile_view']
    reach = a['reach']
    username = a['username']
    logo = a['logo']
    subscribes = a['subscribes']
    impressions = a['impressions']
    reach_not_follower = a['reach_not_follower']
    impressions_from_feed = a['impressions_from_feed']
    file_name_main = main_img(url, type, likes, comments, shares, notes, profile_view, reach, username, logo,
                              carousel_count, video_duration)
    file_name_stat = second_img(profile_view=profile_view, reach=reach, sub=subscribes, impressions=impressions,
                                account=username, reach_not_follower=reach_not_follower, page=impressions_from_feed)
    x = {
        'url1': send_file_url(file_name_main),
        'url2': send_file_url(file_name_stat)
    }
    json_r = json.dumps(x)
    print(json_r)
    return jsonify(json_r)


def main_img(url, type, likes, comments, shares, notes, visits, coverages, username, logo, carousel_count, video_duration):
    img = Image.open(path_main)
    y = input_photo(img, 0, 200, url, type, carousel_count, video_duration)
    input_labels(img, 0, y)
    draw_name(img, 140, font1, username, 'black')
    input_logo(img, 80, logo)
    bright(img, 0.7)
    input_stats(img)
    height_of_content = 980
    height_of_vc = 1105
    draw_like(img, height_of_content, font3, likes)
    draw_comment(img, height_of_content, font3, comments)
    draw_share(img, height_of_content, font3, shares)
    draw_notes(img, height_of_content, font3, notes)
    draw_visits(img, height_of_vc, font3, visits)
    draw_coverage(img, height_of_vc, font3, coverages)
    now = datetime.datetime.now()
    file_name = now.strftime('%d%m%y_%H%M%S') + 'page1_' + username + '.jpg'
    img.save(f'static/media/{file_name}')
    return file_name


def send_file_url(file_name):
    url = url_for('static', filename='media/'+file_name)
    full_url = 'http://192.168.88.41:5000'+url
    return full_url


@app.route('/nurs', methods=['GET'])
def hello():
    return 'hello!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
