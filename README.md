http://docs.jinkan.org/docs/flask/index.html

> pycharm太卡了，最后还是用vscode

https://www.jianshu.com/p/59b8d17b889f

# myctfd

参考 https://github.com/CTFd/CTFd

## 数据表（待完善）

库

```
team(队伍) (tid,teamname)
teammate(队伍成员) (uid,username,password,tid)
challenge_topics(比赛) (topic_id,cname)
challenge(比赛题目)(cid,topic_id,value)
solve(个人解题情况)(score,topic_id,uid)
teamscore(topic_id,tid,solvescore)



```

建库

```
create table team_info(tid int primary key,teamname char(20) unique,website char(20),affiliation char(20),country char(20));

create table user_info(uid int primary key,username char(20) unique not NULL,password char(20) not NULL,tid int,foreign key(tid) references team_info(tid));

create table challenge_topics(topic_id int primary key,cname char(20));

create table challenge(cid int,topic_id int,value int,flag char(40),primary key(cid,topic_id),foreign key(topic_id) references challenge_topics(topic_id));

create table solve(topic_id int,uid int,score int,foreign key(topic_id) references challenge_topics(topic_id),foreign key(uid) references user_info(uid));

create table teamscore(topic_id int,tid int,solvescore int,primary key(topic_id,tid),foreign key(tid) references team_info(tid));


//写触发器
个人score更新
update solve set score = score+500 where uid=1;
update solve set score = score+(select value from challenge where topic_id='100' and cid=1) where uid=1;

//队伍成绩统计
update teamscore set solvescore=(select sum(score) from (select score from solve where uid in (select uid from user_info where tid=1))as a) werehere tid=1;




/*create table solve(score int,topic_id int,uid int,primary key(topic_id,uid),foreign key(topic_id) references challenge_topics(topic_id),foreign key(uid) references user_info(uid));
*/
//select value from challenge where topic_id='' and cid ='';
//insert into solve values(value,topic_id,uid)
//update solve set score=score+value where uid=
//update solve set score = score+(select value from challenge where topic_id='100' and cid=1) where uid=1;

//create table teamscore(topic_id int,tid int,uid int,solvecore int,primary key(topic_id,tid));


//select score from solve where uid in (select uid from user_info where tid=1);

//select score from solve where (select uid from teammate where tid='');
//insert into teamscore value(topic_id,tid,score)
//update teamscore set score='' where tid='';

//insert into 
```
数据库测试语句

```
insert into team_info values(1,'popko','www.popko.com','popax','C');
insert into team_info values(2,'nopppppppp','www.popax.com','popax2','D');

insert into user_info values(1,'pop','poppop',1);
insert into user_info values(2,'sygg','syggtql',1);

insert into challenge_topics values(100,'FCTF');

insert into challenge values(1,100,200,'flag{welcome_to_actf}');
insert into challenge values(2,100,300,'flag{you_got_it}');
insert into challenge values(3,100,500,'flag{easy_rsa}');

insert into solve values(100,1,0);
insert into solve values(100,2,0);
insert into teamscore values(100,1,0);
insert into teamscore values(100,2,0);


update solve set score = score+(select value from challenge where topic_id='100' and cid=1) where uid=2;
update solve set score = score+(select value from challenge where topic_id='100' and cid=2) where uid=2;
update solve set score = score+(select value from challenge where topic_id='100' and cid=3) where uid=1;

update teamscore set solvescore=(select sum(score) from (select score from solve where uid in (select uid from user_info where tid=1))as a) where tid=1;



```








## 功能（待完善）

```
注册/登录
后台
scordboard
teaminfo
userinfo
challengeinfo
题目分类
公告

其他(作为补充)：
wp汇总
付费解锁题目
赛事分类
```

## 备注(for 报告)

### 前端(jinja)

#### {% include %} 标签

```
<body>
	<!-- 导入header.html -->
    {% include 'header.html' %}
    <div class="content">
        中间内容
    </div>
    <!-- 导入footer.html -->
    {% include 'footer.html' %}
</body>
```

with context(将for传入include)

http://docs.jinkan.org/docs/jinja2/templates.html

```html
        {% for challenge in challenges %}
        <div id=triggerBtn-{{challenge.id}} class="col-md-3 d-inline-block tag-密码学">
            <button class="btn btn-dark challenge-button w-100 text-truncate pt-3 pb-3 mb-2" value="2">
                <p>{{challenge.name}}</p><span>{{challenge.value}}</span>
            </button>
        </div>
        {% include "challenge.html" with context %} 
        {% endfor %}
```



#### 模板继承

base.html

```
<title>{% block title %}{% endblock %} - My Webpage</title>
```

extend.html

```
{% extends "basetest.html" %}
{% block title %}Index{% endblock %}
```

要呈现在父模板中定义的块的内容

```
{% block head %}
{{ super() }}
<style type="text/css">
    .important {
        color: #336699;
    }
</style>
{% endblock %}
```

#### 导航栏

collapse navbar-collapse

#### login.html

```
{% extends "base.html" %}
{% block content %}
    login.html
    <form method="post">
        <p>账号：<input type="text" name="username"></p>
        <p>密码：<input type="password" name="password"></p>
        <!--下面的按钮都是提交按钮-->
        <p><input type="submit" value="login"></p>
    </form>
{% endblock %}
```

#### 蓝图

实现**各个模块的视图函数写在不同的py文件中**，在主视图中导入分路由视图的模块，并注册蓝图对象，**降低各个功能模块的耦合度**，使用`flask.Blueprint`定义蓝图，

```python
from flask import Blueprint, redirect, url_for, render_template, session
from utils import auth

_index = Blueprint('index', __name__)


@_index.route('/index', methods=['GET', 'POST'])
def index():
    if not auth():
        return redirect(url_for('login'))
    return render_template("index.html", user=session.get('user'))

```

>  蓝图名字和系统名字出现重叠,改动即可

```python
from index import _index
app.register_blueprint(_index)
```

login.py

```python
def login():
    if auth():
        return redirect(url_for('index.index'))#Blueprint名.函数名
```

#### challenges.html

challenge.html

```
删除 max_attempts
没找到{% block solves %}的模板
```

模态框

```

```

id模糊匹配

```
document.querySelector('[id^="triggerBtn"]');//triggerBtn-1 (challengeid)
querySelectorAll
```

获取子节点

https://blog.csdn.net/laok_/article/details/75760572

#### scoreboard.html

```
删除 score-graph
删除 翻页
```



### 数据库

sqlite3

```
import sqlite3
```

http://docs.jinkan.org/docs/flask/tutorial/dbcon.html



> Flask 提供了两种环境（Context）：应用环境（Application Context）和请求环境（Request Context）。暂且你所需了解的是，不同环境有不同的特殊变量。例如 [`request`](http://docs.jinkan.org/docs/flask/api.html#flask.request) 变量与当前请求的请求对象有关， 而 [`g`](http://docs.jinkan.org/docs/flask/api.html#flask.g) 是与当前应用环境有关的通用变量。我们在之后会深入了解它们
>
> 可以安全地在 [`g`](http://docs.jinkan.org/docs/flask/api.html#flask.g) 对象存储信息
>
> Flask 提供了 [`teardown_appcontext()`](http://docs.jinkan.org/docs/flask/api.html#flask.Flask.teardown_appcontext) 装饰器。它将在每次应用环境销毁时执行

```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myctfd.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "test"
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


# admin = User(uid=1,username='admin', password='123123')
admin = User(username='admin', password='123123')
print(db.session)
print(db.session.add(admin))
print(db.session.commit())
print(db)
```

```
        count = (db.session.query(User.username)
        .filter(User.username ==request.form['username'])
        .filter(User.password == request.form['password'])
        .count())
```

#### sqlite3使用

```
sqlite3 myctfd.db < sqlite.sql #导入
sqlite3 myctfd.db #命令行连接测试

自增
autoincrement

在sqlite中，只有一个整数列是主键时才会获得自动增量行为。复合键可防止自动增量生效。

create table challenge(cid int auto_increment,topic_id int DEFAULT 1,name char(20),category char(20),value int,desc char(40),flag char(40),primary key(cid,topic_id),foreign key(topic_id) references challenge_topics(topic_id));
```

> 用户名模糊查询

#### 触发器

> sqlite中触发器和表(例:solve)绑定,删表后需要重新设置

```
create trigger addSolves after insert on solve
begin
update challenge set solve_count=solve_count+1 where cid=new.cid;
end;

create trigger addSolves after insert on solve begin update challenge set solve_count=solve_count+1 where cid=new.cid; end;
```

```
insert into solve(uid,cid) values(1,2);
select * from challenge;
```



## todo:



