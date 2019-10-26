from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Pagina web IBM'

@app.route('/defaul.html')
def default():
    return 'Segunda prueba'


if __name__ == '__main__':
    app.run(debug = True)

