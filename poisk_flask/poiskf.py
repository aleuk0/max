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
TODO
1. функция для вопроса и отображения числа, а также его подсчета
2. в select надо будет брать a или b, записывать новые значения через
insert, как в /add с методом post
3. сделать шаблон, похожий на poisk_tk.py
4. https://habrahabr.ru/post/321510/ &
https://ruseller.com/lessons.php?rub=28&id=2277
'''

@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select a, b from entries order by id desc limit 1')
    entries = cur.fetchall()
    flash('Number < 500000?' + str(entries))
    return render_template('show_entries.html', entries=entries)
'''
You cannot use an aggregate function like MAX() like this in the selection.
Instead consider the following:
    ORDER BY unixtime DESC to sort the results matching your selection with the
    newest first.
    LIMIT 1 to only return the first result i.e. the newest.
'''

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (a, b) values (?, ?)',
            [request.form['a'], request.form['b']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run()
