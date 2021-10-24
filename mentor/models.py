from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from mentor import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='menteedefault.jpg')
    password = db.Column(db.String(60), nullable=False)
    user_status = db.Column(db.String(20), nullable=False, default='Mentee')
    field= db.Column(db.String(60))
    job = db.Column(db.String(60))
    mentor = db.relationship('UserMentor', backref='user', lazy=True)


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Usermentor(User):
    experience=db.Column(db.Float())
    mentee= db.Column(db.Integer, db.ForeignKey('user.id'))

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}', '{self.mentee}')"



class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fieldtitle = db.Column(db.String(100), nullable=False)
    jobtitle= db.Column(db.String(100), nullable=False)
    avg_salary= db.Column(db.Integer, nullable=False)
    education_req= db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f"User('{self.fieldtitle}', '{self.jobtitle}', '{self.avg_salary}','{self.avg_salary}')"



