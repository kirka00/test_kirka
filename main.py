import base64  # библиотека для работы с битами картинок
from flask import Flask, request
from flask import render_template
app = Flask(__name__)


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


n = 1  # переменная для номер картинки
images = []  # список для хранения названий картинок


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    global n, images, spisok
    if request.method == 'GET':
        return render_template('index.html', images=images)
    elif request.method == 'POST':
        image = request.files['file']  # достём изображение из формы
        bytestring = image.read()  # читаем биты изображения
        image = base64.b64encode(bytestring).decode('utf-8')
        name_image = f"static/img/{n}.txt"
        images.append(image)
        n += 1
        f = open(name_image, "w")
        f.write(image)
        f.close()
        return render_template('index.html', images=images, spisok=spisok)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return render_template('index_2.html')
    elif request.method == 'POST':
        image = request.files['file']  # достём изображение из формы
        bytestring = image.read()  # читаем биты изображения
        image = base64.b64encode(bytestring).decode('utf-8')
        f = open("static/img/1.txt", "w")
        f.write(image)
        f.close()
        return render_template('index_2.html', image=image)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
