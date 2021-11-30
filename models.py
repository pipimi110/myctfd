import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from sqlalchemy.sql.schema import ForeignKey

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
    tid = db.Column(db.Integer)
    
    
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

class Challenge(db.Model):
    __tablename__ = "challenge"
    cid = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    category = db.Column(db.String(20))
    value = db.Column(db.Integer)
    desc = db.Column(db.String(40))
    flag = db.Column(db.String(40))
    solve_count = db.Column(db.Integer)

    def __init__(self, name, category, value, desc, flag):
        self.name = name
        self.category = category
        self.value = value
        self.desc = desc
        self.flag = flag

    def __repr__(self):
        return '<Challenge %r>' % self.name

class Solve(db.Model):
    __tablename__ = "solve"
    topic_id = db.Column(db.Integer)
    uid = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, primary_key=True)

    def __init__(self, uid, cid):
        self.uid = uid
        self.cid = cid

    def __repr__(self):
        return '<Solve %r>' % self.uid


def userName2Tid(name):
    mytid = db.session.query(User.tid).filter(
        User.username == name).one()[0]
    return mytid

def tid2TeamUidList(tid):
    teammate_tuples = db.session.query(
        User.uid).filter(User.tid == tid).all()
    uids = []
    for tuple in teammate_tuples:
        # print(tuple[0])
        uids.append(tuple[0])
    return uids

def userName2TeamUidList(name):
    mytid = userName2Tid(name)
    # print(mytid)
    uids = tid2TeamUidList(mytid)
    return uids

def uids2SolveCids(uids):
    solveCids = []
    teamsolve_tuples = db.session.query(Solve.cid).filter(Solve.uid.in_(uids)).all()
    for tuple in teamsolve_tuples:
        # print()
        solveCids.append(tuple[0])
    return solveCids


def solveCids2ValueSum(solveCids):
    sum = 0
    for cid in solveCids:
        value = db.session.query(Challenge.value).filter(Challenge.cid==cid).one()[0]
        sum += value
    return sum
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
