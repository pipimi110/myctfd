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
create table team_info(tid int primary key,teamname char(20) unique);

create table user_info(uid int primary key,username char(20) unique,password char(20) not NULL,tid int,foreign key(tid) references team_info(tid));

create table challenge_topics(topic_id int primary key,cname char(20));

create table challenge(cid int primary key,topic_id int,value int,foreign key(topic_id) references challenge_topics(topic_id));

create table solve(topic_id int,uid int,score int,foreign key(topic_id) references challenge_topics(topic_id),foreign key(uid) references user_info(uid));

create table teamscore(topic_id int,tid int,solvescore int,primary key(topic_id,tid));


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
insert into team_info values(1,'popko');
insert into team_info values(2,'nopppppppp');

insert into user_info values(1,'pop','poppop',1);
insert into user_info values(2,'sygg','syggtql',1);

insert into challenge_topics values(100,'FCTF');

insert into challenge values(1,100,200);
insert into challenge values(2,100,300);
insert into challenge values(3,100,500);

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

#### todo:

```
搜索功能
新建功能
```



### 数据库

sqlite3

```
import sqlite3
```

