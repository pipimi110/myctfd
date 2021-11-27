# import sqlite3
# from flask import g,Flask
# import os

# app = Flask(__name__)
# # def connect_db():
# #     """Connects to the specific database."""
# #     # rv = sqlite3.connect(app.config['DATABASE'])
# #     rv = sqlite3.connect(DATABASE)
# #     rv.row_factory = sqlite3.Row
# #     return rv

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         path = os.path.dirname(os.path.abspath(__file__))
#         DATABASE = path+'/myctfd.db'
#         # print(DATABASE)
#         db = g._database = sqlite3.connect(DATABASE)
#     return db


# @app.before_request
# def init_db():
#     print("init_db")
#     with app.app_context():
#         db = get_db()
#         sqlfile = 'sqlite.sql'
#         with app.open_resource(sqlfile, mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()

# @app.teardown_appcontext
# def close_connection(exception):
#     print("close_connection")
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()


# @app.route('/test')
# def test():
#     print(get_db())
#     print(getattr(g, '_database', None))
#     return "test"

# if __name__=='__main__':
#     # print(get_db())
#     # app.run(debug=True)
#     init_db()


# from flask_sqlalchemy import create_engine, MetaData

# from flask import Flask
# DB_URI = 'mysql+mysqldb://{}:{}@{}/{}.format(USERNAME，PASSWORD，HOSTNAME，PORT，DATABASE)'
# DB_URI = 'sqlite:///myctd.db'#sqlite://<nohostname>/<path>
# # engine = create_engine('sqlite:///foo.db', echo=True)
# engine = create_engine(DB_URI, echo=True)
# metadata = MetaData(engine)
# # 创建数据库引擎
# engine = create_engine(DB_URI)
# app = Flask(__name__)
# db = SQLAlchemy(app)  # 通过类`SQLAlchemy`来连接数据库
# print(db)





