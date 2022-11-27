import log
from multiprocessing import Process

from web.apiv1 import apiv1_bp

from app.brushtask import BrushTask
from app.db import init_db, update_db
from app.helper import IndexerHelper
from app.rsschecker import RssChecker
from app.scheduler import run_scheduler
from app.sync import run_monitor
from check_config import update_config, check_config
from version import APP_VERSION
from web.main import App


def init_system():
    # 配置
    log.console('NAStool 当前版本号：%s' % APP_VERSION)
    # 数据库初始化
    init_db()
    # 数据库更新
    update_db()
    # 升级配置文件
    update_config()
    # 检查配置文件
    check_config()


def start_service():
    log.console("开始启动进程...")
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


# 系统初始化
init_system()


# 启动服务
start_service()
