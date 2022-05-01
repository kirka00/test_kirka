import base64
from turtle import title  # библиотека для работы с битами картинок
from flask import Flask, request, render_template
import json
from random import randint
app = Flask(__name__)


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/member')
def member():
    with open("templates/astro.json", "rt", encoding="utf8") as f:
        list_ = json.loads(f.read())
    return render_template('member.html', list_=list_[f"{randint(1, 3)}"])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
