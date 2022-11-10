import os
import datetime
from flask import Flask

"""
实例化flask的实例，进行初始化
"""
App = Flask(__name__)
App.config['JSON_AS_ASCII'] = False
App.secret_key = os.urandom(24)
App.permanent_session_lifetime = datetime.timedelta(days=30)
