from flask import Flask
from flask import render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager,UserMixin,login_user, logout_user,login_required,current_user
from book import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "ENTER YOUR SECRET KEY"

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.init_app(app)

#class for user database

class Users(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(250), unique = True, nullable = False)
    password = db.Column(db.String(250),unique = True, nullable = False)

#class for class booking

class ClassroomBookings(db.Model):
    id = db.Column(db.Integer,unique = True, primary_key = True)
    classroom = db.Column(db.String(10),nullable = False)
    consumer = db.Column(db.String(250),nullable = False)
    timeslot = db.Column(db.Integer,nullable = False)
    date = db.Column(db.Date, nullable= False)
    status = db.Column(db.Integer, nullable = True)


db.init_app(app=app)
with app.app_context():
    db.create_all()

@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)

#home page  

@app.route('/home')
@app.route('/')
def home():
    return render_template('login.html')

#all methods related to user authentication

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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    print("a")
    return redirect('/')

#dashboard controls

@app.route('/dashboard')
@login_required
def dashboard():    
    return render_template("home.html")


classes = ['UG1','UG2','UG3','UG4']

@app.route('/classroom')
@login_required
def classroom():
    #create a json data to send to the frontend to display the available timeslots and classrooms
    for i in classes:
        print(ClassroomBookings.query.filter_by(classroom = i).all())
    b = Users.query.all()
    c = []
    for i in b:
        c.append(i.mapping)
    print(c)
    return render_template('classroomcalendar.html')

@app.route('/classroomBook',methods = ['POST'])
@login_required
def book_classroom():
    if request.method == "POST":
        createBooking(db,request.form.get('classroomName'),current_user.username, request.form.get('timeslot'),request.form.get('date'),0)

@app.route('/labs')
@login_required
def labs():
    return render_template('labcalendar.html')

@app.route('/transport')
@login_required
def transport():
    return render_template('transportationcalendar.html')




if __name__ == '__main__':      
    app.run()

    