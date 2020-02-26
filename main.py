#@timofeeevzh 

from flask import Flask, escape, request, render_template
import templates
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
    return f'{a},{b},{c}'

@app.route('/second', methods=['GET','POST'])
def second():
    if  request.method == 'GET':
        return render_template('./second2.html')
    if request.method == 'POST':
        list1 = request.form.get('text')
        turn=[x for x in reversed(list1)]
        s=''
        print(list1)
        return f'{list1[::-1]}{s.join(list(reversed(list1)))}{s.join(turn)}'

if __name__ == '__main__':
    app.run('0.0.0.0')
