from flask import Flask
from flask import request #載入 request 物件
from flask import redirect
from flask import render_template
from flask import session
import os

app = Flask( __name__, static_folder='static', static_url_path='/')
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/signin', methods=['POST'])
def singin():
  account=request.form['account']
  password=request.form['password']
  if (account == 'test' and password == 'test'):
    session['isLogin'] = True
    return redirect('/member')
  else:
    return redirect('/error')

@app.route('/member')
def member():
  isLogin = session.get('isLogin')
  if (isLogin):
    return render_template('member.html')
  else:
    return redirect('/')

@app.route('/error')
def error():
  return render_template('error.html')

@app.route('/signout')
def signout():
  session['isLogin'] = False
  return redirect('/')

app.run(port=3000)