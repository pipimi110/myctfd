from flask import Blueprint, redirect, url_for, render_template, session
from flask.globals import request
from models import db,Challenge
from userAuth import auth

_dchallenge = Blueprint('dchallenge', __name__)
#cic topics_id challenge_name category score descri flag solvecount
#
#
#
#__init__(self, name, category, value, desc, flag):

@_dchallenge.route('/dchallenge', methods=['GET', 'POST'])
def dchallenge():
    if not auth():
        return redirect(url_for('userAuth.login'))
    elif session.get('user')!="admin":
        return redirect(url_for('challenges.challenges'))

    if request.method=='POST':
        '''if request.form["cid"]!= None and request.form["topics_id"]!= None and request.form["name"]!= None and request.form["category"]!= None and request.form["value"]!= None and request.form["desc"]!= None and request.form["flag"]!= None and request.form["solve_count"]!= None:
            new_challenge=Challenge(request.form['cid'],request.form['topics_id'],request.form['name'],request.form['category'],request.form['value'],request.form['desc'],request.form['flag'],request.form['solve_count'])
            db.session.add(new_challenge)
            return redirect(url_for('challenges'))'''
        #if request.form["cid"] != None and request.form["category"] != None and request.form["value"] != None and request.form["desc"] != None and request.form["flag"] != None:
        if request.form["cid"] !=None:
            del_challenge=db.session.query(Challenge.cid).filter(Challenge.cid==request.form["cid"])
            if del_challenge:
                db.session.query(Challenge).filter(Challenge.cid == request.form["cid"]).delete()
                #db.session.query(Challenge).delete(del_challenge)
                db.session.commit()
            return redirect(url_for('challenges.challenges'))
    return render_template("dchallenge.html",user=session.get('user'))
