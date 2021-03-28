from app import db


class User(db.Model):
    phone_number = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(30), nullable=False)
    nickname = db.Column(db.String(20), nullable=False, unique=True)


class Message(db.Model):
    sender_phone = db.Column(db.String(20), db.ForeignKey('sender.phone_number'))
    sender = db.relationship('User', backref=db.backref('sent_massages', lazy=True))
    recipient_phone = db.Column(db.String(20), db.ForeignKey('recipient.phone_number'))
    recipient = db.relationship('User', backref=db.backref('received_massages', lazy=True))


class Friendship(db.Model):
    friend1_phone = db.Column(db.String(20), db.ForeignKey('user.phone_number'))
    friend2_phone = db.Column(db.String(20), db.ForeignKey('user.phone_number'))
    user = db.relationship('User', backref=db.backref('friends', lazy=True))
