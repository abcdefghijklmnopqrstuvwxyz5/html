from flask import Flask, url_for, request
import random as rd

app = Flask(__name__)

text = ['Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!']

colors = ['success', 'primary', 'danger', 'warning', 'info']

@app.route('/promotion_image')
def mars_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='images/MARS.png')}">
                    <p class="alert alert-{rd.choice(colors)}">{text[0]}</p>
                    <p class="alert alert-{rd.choice(colors)}">{text[0]}</p>
                    <p class="alert alert-{rd.choice(colors)}">{text[0]}</p>
                    <p class="alert alert-{rd.choice(colors)}">{text[0]}</p>
                    <p class="alert alert-{rd.choice(colors)}">{text[0]}</p>
                  </body>
                </html>"""

@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronauts():
    if request.method == 'GET':
        return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style2.css')}"/>
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                    <h1 align="center">Анкета претендента</h1>
                    <h2 align="center">на участие в миссии</h2>
                    <div>
                        <form class="appliсation_form" method="POST">
                            <input type="text" class="form-control" id="text" placeholder="Введите фамилию" name="text">
                            <input type="text" class="form-control" id="text" placeholder="Введите имя" name="text">
                  </body>
                </html>"""


@app.route('/')
def mission_name():
    return 'Миссия Колонизация Марса'

@app.route('/index')
def mission_slogan():
    return 'И на Марсе будут яблони цвести!'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')