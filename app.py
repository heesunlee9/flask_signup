import os
from flask import Flask
from flask import request
from flask import redirect 
from flask import session
from flask import render_template
from models import db
from flask_wtf.csrf import CSRFProtect # cross-site request forgery
from forms import RegisterForm, LoginForm
from models import Fcuser
# create an object
app = Flask(__name__) 

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('userid', None)
    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['userid'] = form.data.get('userid')
        return redirect('/')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        fcuser = Fcuser() 
        fcuser.userid = form.data.get('userid')
        fcuser.username = form.data.get('username')
        fcuser.password = form.data.get('password') 
        
        db.session.add(fcuser)
        # Commmit is done automatically because of 'app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True'
        # Nonetheless, we explicitly commit again.
        db.session.commit() 
                
        return redirect('/')
    return render_template('register.html', form=form)

    # We don't have to do check method
    # if request.method == 'POST': 
    #     We don't have to get data 
    #     userid = request.form.get('userid')
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     re_password = request.form.get('re-password')

    #     if (userid and username and password and re_password) and password == re_password:
    #         fcuser = Fcuser() 
    #         fcuser.userid = form.data.get('userid')
    #         fcuser.username = form.data.get('username')
    #         fcuser.password = form.data.get('password') 
        
        #     db.session.add(fcuser)
        #     Commmit is done automatically because of 'app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True'
        #     Nonetheless, we explicitly commit again.
        #     db.session.commit() 
        #     print('Success!')
                    
        #     return redirect('/')
    # return render_template('register.html', form=form)

# class Test(db.Model):
#     __tablename__ = 'test_table'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(32), unique=True)

# # create a dbfile
# db.create_all()

@app.route('/')
def hello():
    userid = session.get('userid', None)
    return render_template('hello.html', userid=userid)

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

# setting for alchemy
# ... = 'mysql:///' + id + password + address + the location this db is running
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'qiowejroiqwafaf'

csrf = CSRFProtect()
csrf.init_app(app)

db.init_app(app)
db.app = app
db.create_all()

# To execute app.py, we can use python(python app.py) 
# instead of Flask instruction(FLASK=APP=app.py flask run)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)










































