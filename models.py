import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{path}/myctfd.db'.format(
    path=path)
db = SQLAlchemy(app)


class User(db.Model):
    # __tablename__ = "test"
    __tablename__ = "user_info"
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

class Team(db.Model):
    __tablename__ = "team_info"
    tid = db.Column(db.Integer, primary_key=True)
    teamname = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    website = db.Column(db.String(20))
    affiliation = db.Column(db.String(20))
    country = db.Column(db.String(20))

    def __init__(self, teamname, password):
        self.teamname = teamname
        self.password = password

    def __repr__(self):
        return '<Team %r>' % self.teamname


# def init_db():
#     db.create_all()
#     # Create a test user
#     # admin = User(username=myutils.get_random_id(), password=myutils.get_random_id())
#     # admin = User(username=get_random_id(), password=get_random_id())
#     admin = User(username="admin", password="123123")
#     db.session.add(admin)
#     db.session.commit()
# if __name__ == '__main__':
#     init_db()
# admin = User(uid=1,username='admin', password='123123')
