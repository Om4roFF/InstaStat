import time

from flask import Flask, send_file, send_from_directory, request
from PIL import ImageFont

from full_stat import second_img
from photo_builder import bright, input_photo, input_labels, input_stats, input_logo
from draw_image import draw_name, draw_like, draw_comment, draw_share, draw_notes, draw_visits, draw_coverage
from photo_builder import img
font1 = ImageFont.truetype('FontsFree-Net-arial-bold.ttf', 28)
font2 = ImageFont.truetype("arial.ttf", 42)
font3 = ImageFont.truetype("arial.ttf", 32)


app = Flask(__name__)


@app.route('/get_image1', methods=['POST'])
def home():
    json_string = request.stream.read().decode('utf-8').strip()

    print(json_string)
    main_img(4, 2, 12, 4, 1, 2, 4, 6, 1, 2)
    time.sleep(6)
    return send_file(filename_or_fp='media/ws1.jpg', mimetype='image/jpg')


@app.route('/get_image2', methods=['GET', 'POST'])
def second():
    second_img(31,62,13,2,1,2,1,'31', '31')
    time.sleep(6)
    return send_file(filename_or_fp='media/ws2.jpg', mimetype='image/jpg')


def main_img(url, type, likes, comments, shares, notes, visits, coverages, name, logo):
    y = input_photo(0, 200, 'C:\\Users\\admin\\PycharmProjects\\InstaStatistics\\scrip.jpg', 'video')
    input_labels(0, y)
    draw_name(140, font1, 'twitter', 'black')
    input_logo(80, 'static/igtv-logo-circle-black-and-white.png')
    bright(0.7)
    input_stats()
    height_of_content = 980
    height_of_vc = 1105
    draw_like(height_of_content, font3, 1020)
    draw_comment(height_of_content, font3, 100)
    draw_share(height_of_content, font3, 160)
    draw_notes(height_of_content, font3, 26)
    draw_visits(height_of_vc, font2, 8)
    draw_coverage(height_of_vc, font2, 9468)
    img.save('media/ws1.jpg')
    img.show()


if __name__ == '__main__':
    app.run(debug=False)


# second_img(31,62,13,2,1,2,1,'31','31')
# main_img(3,31,2,1,5,1, 2, 3, 1, 3)