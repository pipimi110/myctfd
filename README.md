http://docs.jinkan.org/docs/flask/index.html

> pycharm太卡了，最后还是用vscode

https://www.jianshu.com/p/59b8d17b889f

# myctfd

参考 https://github.com/CTFd/CTFd

## 数据表（待完善）

```
team(队伍)(id,name,token,得分,解题状态)
teammate(队伍成员)(id,name,password,得分)
challenge(题目)(id,描述（包括链接），类别，hint，分数,解题人数)
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



### 数据库

sqlite3

```
import sqlite3
```

