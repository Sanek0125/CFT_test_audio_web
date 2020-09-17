
from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Привет, это тестовое задание CFT'

@app.route('/upload')
def upload():
    return 'Загрузи свою любимую песню'



# Примеры:
@app.route('/mp3/<your_name_file>')
def show_name_file(your_name_file):
    return 'Привет, имя твоего файла: %s' % escape(your_name_file)
    
@app.route('/integer_example/<int:my_number>')
def show_post(my_number):
    # show the post with the given id, the id is an integer
    return 'My number is %d' % my_number
