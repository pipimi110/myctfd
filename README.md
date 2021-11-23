# flask

http://docs.jinkan.org/docs/flask/index.html

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

**外部可访问的服务器+自定义端口**

```
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
```

**调试模式**

```
app.debug = True
app.run()
```

另一种是作为 run 方法的一个参数传入:

```
app.run(debug=True)
```

## 路由

### 匹配 URL

```
@app.route('/user/<username>')
def show_user_profile(username):

@app.route('/post/<int:post_id>')
def show_post(post_id):
```

```
@app.route('/projects/') #少了/会自动补全
@app.route('/about') #多了/会报404
```

### 生成 URL

```python
@app.route('/api/<number>', methods=['GET', 'POST'])
def api_func(number):
    print(url_for('hello'))
    print(url_for('hello', name='popko'))
    print(url_for('api_func', number=1))
    return 'api'
```

## 重定向和错误

```
from flask import redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))
```

404

```

```



## 请求request

> from flask import request

默认的请求方式只有GET，其他请求都需要通过参数methods进行指定

```
@app.route('/', methods=['GET', 'POST'])
```

**获取请求参数**

GET

```
request.agrs.get('参数名')
```

POST

```csharp
request.form.get('参数名')
```

```
request.method
request.host
request.base_url
request.files
```

## 响应

make_response()，相当于DJango中的HttpResponse。

**返回内容**

```python
    response = make_response('<h2>羞羞哒</h2>')
    return response, 404
```

**返回页面**

```python
    temp = render_template('hello.html')
    response = make_response(temp)
    return response
```

不能直接写做：make_response('hello.html')，必须用render_template('hello.html')形式。

**返回状态码**

```
    response = make_response(temp, 200)
    return response
```

```
    response = make_response(temp)
    return response, 200
```

## 跳转(redirect)

flask中的 redirect 相当于 DJango中的 HttpResponseRedirect。

```
return redirect('/hello/index/')
```

url_for(函数名)

```
return redirect(url_for('first.index'))
return redirect(url_for('hello_world'))
//@app.route('/')
def hello_world():
```

## 静态文件(css、js)

存储在文件系统上的 `static/style.css`

```
url_for('static', filename='style.css')
```

## 模板渲染(html)

```
from flask import render_template
```

Flask 配备了 [Jinja2](http://jinja.pocoo.org/) 模板引擎

Flask 会在 **templates** 文件夹里寻找模板

```
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

```
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %}
```

在模板里，你也可以访问 [`request`](http://docs.jinkan.org/docs/flask/api.html#flask.request) 、 [`session`](http://docs.jinkan.org/docs/flask/api.html#flask.session) 和 [`g`](http://docs.jinkan.org/docs/flask/api.html#flask.g) [[1\]](http://docs.jinkan.org/docs/flask/quickstart.html#id10) 对象， 以及 [`get_flashed_messages()`](http://docs.jinkan.org/docs/flask/api.html#flask.get_flashed_messages) 函数。

自动转义功能默认是开启的，所以如果 name 包含 HTML ，它将会被自动转义。如果你能信任一个变量，并且你知道它是安全的（例如一个模块把 Wiki 标记转换为 HTML），你可以用 `Markup` 类或 `|safe` 过滤器在模板中把它标记为安全的。

```
<h1>Hello {{ name | safe }}!</h1>
```

> 可能导致xss

### 请求对象

### 文件上传

## session/Cookies

Flask Sessions（会话）

与Cookie不同，**Session（会话）**数据存储在服务器上。会话是客户端登录到服务器并注销服务器的时间间隔。需要在该会话中保存的数据会存储在服务器上的临时目录中。

为每个客户端的会话分配**会话ID**。会话数据存储在cookie的顶部，服务器以加密方式对其进行签名。对于此加密，Flask应用程序需要一个定义的**SECRET_KEY**。

```
from flask import session
import uuid
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.secret_key = uuid.uuid4().bytes
```

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            session['username'] = request.form['username']
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/index', methods=['GET', 'POST'])
def index():
    print(session)
    name = None
    if "logged_in" in session:
        name = session["username"]
    return render_template("index.html", name=name)

```



# pycharm

> 太卡了，最后还是用vscode

## 坑

https://www.jianshu.com/p/59b8d17b889f

# myctfd

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

