#@timofeeevzh 
import requests
from flask import Flask, escape, request, render_template
from classes import DeckOfCards

app = Flask(__name__)
deck = DeckOfCards()

@app.route('/')
def hello():
    name = request.args.get("name", "Timofeev Evgeniy TS-81")
    return f'{name}'

@app.route('/first')
def helloo():
    a = None
    b = 999999999999999999999999
    c = 'dead inside'
    return f'{a}, {b}, {c}'

@app.route('/second', methods=['GET','POST'])
def second():
    if  request.method == 'GET':
        return render_template('./second2.html')
    if request.method == 'POST':
        text = request.form.get('text')
        rev1=text[::-1] #slice
        rev2="".join(list(reversed(text))) #reversed
        rev3="".join([x for x in reversed(text)]) #comprehension
        return f'$lice: {rev1}</br>rever$ed: {rev2}</br>comprehen$ion: {rev3}</br>'

@app.route('/third', methods=['GET','POST'])
def third():
    if  request.method == 'GET':
        return render_template('./third.html',content='\u0020',  deck=str(deck))
    else:
        if "shuffle" in request.form:
            deck.shuffle()
            text = "Shuffled!"
        elif "pop" in request.form:
            text = deck.pop()
        elif "get_random" in request.form:
            text = deck.getrand()
        else:
            num = request.form.get("text")
            text = deck.index(num)
        return render_template('./third.html',content=text, deck=str(deck))

@app.route('/fourth/1', methods = ['GET','POST'])
def fourth1():
    if request.method == 'GET':
            return render_template('./fourth.html')
    if request.method == 'POST':
        text1 = request.form.get('text1')
        text2 = request.form.get('text2')
        x = range(int(text1),int(text2))
        x1= list(filter(lambda x: not x%3,x))
        return f'{x1}'

#@app.route('/fourth/2', methods = ['GET', 'POST'])
#def fourth2():
 #   if request.method == "GET":
  #      return render_template('./fourth2.html')
   # if request.method == 'POST':
    #    text3=request.form.get('text3')
    
   # if len(text3) == 0: 
   #     return f'1.False'
   # else: 
#    return f'1.True'
 #   
  #  if (not text3%2):
   #     return f'2.'

@app.route('/fifth', methods = ['GET','POST'])
def fifth():
    if request.method == 'GET':
        return render_template('./fifth.html')
    if request.method == 'POST':
        username = request.form.get('text')
        github_api_file_url = '/https:/api.github.com/users/<username>'

if __name__ == '__main__':
    app.run('0.0.0.0')
