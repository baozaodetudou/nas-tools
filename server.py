import os
import sys
from config import Config
from web.main import App as nastool
from app.brushtask import BrushTask
from app.helper import IndexerHelper
from app.rsschecker import RssChecker
from app.scheduler import run_scheduler
from app.sync import run_monitor


# 添加第三方库入口,按首字母顺序，引入brushtask时涉及第三方库，需提前引入
with open(os.path.join(os.path.dirname(__file__),
                       "third_party.txt"), "r") as f:
    third_party = f.readlines()
    for third_party_lib in third_party:
        sys.path.append(os.path.join(os.path.dirname(__file__),
                                     "third_party",
                                     third_party_lib.strip()).replace("\\", "/"))

config = Config()
__web_host = "::"
__web_port = 3000
__ssl_cert = None
__ssl_key = None

app_conf = config.get_config('app')
if app_conf:
    if app_conf.get("web_host"):
        __web_host = app_conf.get("web_host")
    __web_port = int(app_conf.get('web_port')) if str(app_conf.get('web_port', '')).isdigit() else 3000
    __ssl_cert = app_conf.get('ssl_cert')
    __ssl_key = app_conf.get('ssl_key')


app_arg = dict(host=__web_host, port=__web_port, debug=False, threaded=True, use_reloader=False)
if __ssl_cert:
    app_arg['ssl_context'] = (__ssl_cert, __ssl_key)


# 启动定时服务
run_scheduler()

# 启动监控服务
run_monitor()

# 启动刷流服务
BrushTask()

# 启动自定义订阅服务
RssChecker()

# 加载索引器配置
IndexerHelper()


if __name__ == '__main__':
    nastool.run(**app_arg)
