from flask import Flask,render_template,request,redirect,session
from db import Database
import api

app=Flask(__name__)


dbo=Database()
#This is the decoretor and this is the syntx to write the code
#Or es decoreter ke andar ak function banana he
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=['Post'])
def perform_registration():
    name=request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response=dbo.insert(name,email,password)

    if response:
        return render_template('login.html',message="Resigtration Sucessful. Kindly login to Proceed")
    else:
        return render_template('register.html',message="Email already exist")

@app.route('/perform_login', methods=['post'])
def perform_login():

    email = request.form.get('user_ka _email')
    password = request.form.get('user_ka_password')

    response=dbo.search(email,password)
    if response:
      return redirect('/profile')
    else:
      return render_template('login.html',message="incorrect email/passwword")

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    text=request.form.get('ner_text')
    response=api.ner(text)
    print(response)

    return render_template("ner.html",response=response)


app.run(debug=True) # es function ko write krke he apka code exute hoga




















# Apne pahile flask class ka ak object bnaya
# frlask me ak important chij hotihe ki ap route import krte ho
# route ky hote he enko ap url bol skte ho so ap ulr create krte ho .
# Apne bola kohi agar slash ur marega top def function execute ho jayega or jo bi lika hoga ho screen pe chala jayega
# apki website ka nam like slash marega or enter marega to es function ke andar jo bi lika he ho execute hoga
#debug=True krne se apko bar bar run krne ki jarurt nhi he
# Flask ke se kam krta he to jese hi jb kohi user es url pe hit krta he slash vale url pe hit krta he
# to inside route function ka code execute hota he jo usme string he ho bej deta he
# IN web developement one is a client and one is a servere , server meanis jaha pe web site ki sari pahile raki uhi he
# or client kon hote he amra re user to jo flask hota he na heo ser ver pe run hota he ho hame sha
# html,javascript,css pile ko bjta he client ke side pr ya broser bol skte he
# ap return ke value baj kr kr ke value baj skte ho client ke sat
# or he route je se alag alag route bnayege
# apke jo bi html filer hogi ho eshi template nam ke folder me hogi ani he nav asej write krave lagnar ahe tu templates
#cha jage varti dusre kahi salman ya patil naih write karu shkto this as to be name templates ko s laga hona chahe
# Render templates render tamplates ka kam kya hota he ho html files ko load krta he  tr return mabde runder template write
#krnar ani tya made ulr patvnatr