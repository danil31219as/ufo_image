from flask import Flask
from flask import render_template
from flask import request
from PIL import Image

app = Flask(__name__)


@app.route('/table/<sex>/<int:age>')
def index(sex, age):
        if sex == 'male':
            Image.new('RGB', (900, 600), (0, 0, 255)).save('static/img/sex.png')
        elif sex == 'female':
            Image.new('RGB', (900, 600), (255, 0, 0)).save('static/img/sex.png')
        else:
            Image.new('RGB', (900, 600), 'grey').save('static/img/sex.png')
        main_image = 'yes' if age >= 21 else 'no'
        return render_template('table.html', ufo=main_image)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
