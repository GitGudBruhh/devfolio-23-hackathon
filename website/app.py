from flask import Flask
from flask import render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager,UserMixin,login_user, logout_user,login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "ENTER YOUR SECRET KEY"

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.init_app(app)

class Users(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(250), unique = True, nullable = False)
    password = db.Column(db.String(250),unique = True, nullable = False)

db.init_app(app=app)
with app.app_context():
    db.create_all()

@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)
@app.route('/home')
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == "POST":
        print("a")
        user = Users.query.filter_by(
            username = request.form.get("username")).first()
        if user.password == request.form.get("password"):
            login_user(user)
            return redirect("/dashboard")
    return render_template("login.html")

@app.route('/signup',methods = ['POST','GET'])
def signup():
    if request.method == "POST":
        print("a")
        user = Users(username = request.form.get("username"),
                    password = request.form.get("password"))
        db.session.add(user)
        db.session.commit()
        
        return redirect('/dashboard')
    return render_template("login.html")

@app.route('/dashboard')
@login_required
def dashboard():    
    return render_template("home.html")

@app.route('/classroom')
@login_required
def classroom():
    return render_template('classroomcalendar.html')

@app.route('/labs')
@login_required
def labs():
    return render_template('labcalendar.html')

@app.route('/transport')
@login_required
def transport():
    return render_template('transportationcalendar.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    print("a")
    return redirect('/')


if __name__ == '__main__':
    app.run()

    