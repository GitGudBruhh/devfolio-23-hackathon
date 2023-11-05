from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ClassroomBookings(db.Model):
    id = db.Column(db.Integer,unique = True, primary_key = True)
    classroom = db.Column(db.String(10),nullable = False)
    consumer = db.Column(db.String(250),nullable = False)
    timeslot = db.Column(db.Integer,nullable = False)
    date = db.Column(db.Date, nullable= False)
    status = db.Column(db.Integer, nullable = True)


def createBooking(db, classroomName, consumer, timeslot, date, status):
    booking = ClassroomBookings(
        classroom = classroomName,
        consumer = consumer,
        timeslot = timeslot,
        date = date,
        status = status
    )
    try:
        db.session.add(booking)
        db.session.commit()
        return 1
    except Exception as e:
        return e
    
def deleteBooking(classobj,consumer,classroomName, date):
    try:
        db.session.delete(ClassroomBookings.query.filter_by(consumer = consumer, classroomName = classroomName, data = date).first())
        return 1
    except Exception as e:
        print(e)
    
def findBookingsByConsumerName(consumer):
    return ClassroomBookings.query.filter_by(consumer= consumer).all()