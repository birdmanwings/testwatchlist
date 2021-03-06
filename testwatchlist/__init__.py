import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path),
                                                              os.getenv('DATABASE_FILE', 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接收用户的ID作为参数
    from testwatchlist.models import User  # 用ID作为User模型的主见查询对应的用户
    user = User.query.get(int(user_id))
    return user  # 返回用户对象


login_manager.login_view = 'login'  # 用login_required装饰器将未登录的用户导向登录页面


@app.context_processor  # 模板上下文处理函数，将user字典统一注入到每个模板的上下文环境中，可以直接在模板中使用
def inject_user():
    from testwatchlist.models import User
    user = User.query.first()
    return dict(user=user)


from testwatchlist import views, errors, commands
