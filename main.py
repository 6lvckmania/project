#@timofeeevzh y

from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Timofeev Evgeniy TS-81'

@app.route('/first')
def helloo():
    a = None
    b = 124124
    c = 'fafew'
    return f'{a}, {b}, {c}'

if __name__ == '__main__':
    app.run('0.0.0.0')
