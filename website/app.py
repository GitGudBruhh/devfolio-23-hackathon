from flask import Flask
from flask import render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager,UserMixin,login_user, logout_user,login_required,current_user
from datetime import datetime
import pandas as pd

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
    time_start = db.Column(db.String(250),nullable = False)
    time_end = db.Column(db.String(250),nullable = False)
    date = db.Column(db.Date, nullable= False)
    status = db.Column(db.Integer, nullable = True)


class LabBookings(db.Model):
    id = db.Column(db.Integer,unique = True, primary_key = True)
    classroom = db.Column(db.String(10),nullable = False)
    consumer = db.Column(db.String(250),nullable = False)
    time_start = db.Column(db.String(250),nullable = False)
    time_end = db.Column(db.String(250),nullable = False)
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

    options = []
    return render_template("home.html", option = options)


classes = ['UG1','UG2','UG3','UG4']

@app.route('/classroom')
@login_required
def classroom():
    print(ClassroomBookings.query.get(1).classroom)
    #create a json data to send to the frontend to display the available timeslots and classrooms
    
    return render_template('classroomcalendar.html')

@app.route('/classroom/book',methods = ['POST','GET'])
@login_required
def book_classroom():

    if request.method == "POST":
        #check availability
        print()
        booking = ClassroomBookings(classroom = request.form.get('classroomName'),
                          consumer = current_user.username, 
                          time_start = request.form.get('time_start') ,#datetime.strptime(request.form.get('time_start'),'%H:%M').time(),
                          time_end = request.form.get('time_end'),#datetime.strptime(request.form.get('time_end'),'%H:%M').time(),
                          date = datetime.strptime(request.form.get('date'),'%Y-%M-%S').date(),
                          status = 0)
        db.session.add(booking)
        db.session.commit()
        return redirect('/dashboard')
    return redirect('/classroom')

@app.route('/labs')
@login_required
def labs():
    return render_template('labcalendar.html')

@app.route('/labs/book')
@login_required
def book_lab():
    if request.method == "POST":
        #check availability
        print()
        booking = LabBookings(classroom = request.form.get('classroomName'),
                          consumer = current_user.username, 
                          time_start = request.form.get('time_start') ,#datetime.strptime(request.form.get('time_start'),'%H:%M').time(),
                          time_end = request.form.get('time_end'),#datetime.strptime(request.form.get('time_end'),'%H:%M').time(),
                          date = datetime.strptime(request.form.get('date'),'%Y-%M-%S').date(),
                          status = 0)
        db.session.add(booking)
        db.session.commit()
        return redirect('/dashboard')
    return redirect('/')


@app.route('/events')
@login_required
def transport():
    return render_template('transportationcalendar.html')

@app.route('/events/book',methods = ['POST','GET'])
@login_required
def book_event():
    if request.method == "POST":
        #check availability
        print()
        booking = ClassroomBookings(classroom = request.form.get('classroomName'),
                          consumer = current_user.username, 
                          time_start = request.form.get('time_start') ,#datetime.strptime(request.form.get('time_start'),'%H:%M').time(),
                          time_end = request.form.get('time_end'),#datetime.strptime(request.form.get('time_end'),'%H:%M').time(),
                          date = datetime.strptime(request.form.get('date'),'%Y-%M-%S').date(),
                          status = 0)
        db.session.add(booking)
        db.session.commit()
        return redirect('/dashboard')
    return redirect('/events')

@app.route('/contact')
def contact():
    return render_template("contactus.html")

if __name__ == '__main__':      
    app.run()

    