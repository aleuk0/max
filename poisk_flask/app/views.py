from flask import render_template
from app import app

a, b = 1000000, 1

@app.route('/')
@app.route('/index')
def index():
    global a, b
    a, b = 1000000, 1
    return render_template('index.html',
                           title='New game',
                           text = '''Let\'s play!
                           Your number must be from 1 to 1000000! ''',
                           number = 'Your number < 500000?')

@app.route('/yes', methods=['POST'])
def yes():
    global a, b
    a = ((a+b)/2)
    if round(a)==round(b):
        return render_template('index.html',
                               title='Yes',
                               text = 'Your number is ',
                               number = round(a))
    return render_template('index.html',
                           title='Yes',
                           text = 'Your number < ',
                           number = round(a,2))

@app.route('/no', methods=['POST'])
def no():
    global a, b
    b = ((a+b)/2)
    if round(a)==round(b):
        return render_template('index.html',
                               title='Yes',
                               text = 'Your number is ',
                               number = round(b))
    return render_template('index.html',
                           title='No',
                           text = 'Your number < ',
                           number = round(b,2))
