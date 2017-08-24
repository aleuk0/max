# все импорты
import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
render_template, flash

# конфигурация
DATABASE = '/tmp/poiskf.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# создаём наше маленькое приложение :)
app = Flask(__name__)
app.config.from_object(__name__)
# Загружаем конфиг по умолчанию и переопределяем в конфигурации часть
# значений через переменную окружения
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'poiskf.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('POISKF_SETTINGS', silent=True)

def connect_db():
    """Соединяет с указанной базой данных."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


'''
Теперь мы можем из командной оболочки Python импортировать и вызвать эту
функцию, тем самым создав базу данных:
>>> from flaskr import init_db
>>> init_db()

>>> from sys import path - ввести, если команда import не выполняется
'''
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    """Если ещё нет соединения с базой данных, открыть новое - для
    текущего контекста приложения
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

'''
1. тут будет функция
@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)

2. только в select надо будет брать a или b, записывать новые значения через
insert, как в /add с методом post
3. сделать шаблон, похожий на poisk_tk.py
4. https://habrahabr.ru/post/321510/ &
https://ruseller.com/lessons.php?rub=28&id=2277


'''


if __name__ == '__main__':
    app.run()
