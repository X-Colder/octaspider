from __future__ import absolute_import # 拒绝隐式引入，因为celery.py的名字和celery的包名冲突，需要使用这条语句让程序正确地运行
from celery.schedules import crontab
from datetime import timedelta


CELERY_IMPORTS = ('tasks')
task_ignore_result = False
broker_host = '10.40.35.39'
broker_port = 5672
broker_url = 'amqp://admin:admin@10.40.35.39:5672//'
#CELERY_RESULT_BACKEND = 'amqp'
result_backend = 'mongodb'
result_backend_settings = {
        "host": "127.0.0.1",
        "port": 27017,
        "database": "jobs",
        "taskmeta_collection": "stock_taskmeta_collection",
}



task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = "Asia/Shanghai"  # 时区设置
worker_hijack_root_logger = False  # celery默认开启自己的日志，可关闭自定义日志，不关闭自定义日志输出为空
result_expires = 60 * 60 * 24  # 存储结果过期时间（默认1天）

# 导入任务所在文件
imports = [
    "stock_tasks.stocks.get_realtime_data",  # 导入py文件
]


# 需要执行任务的配置
beat_schedule = {
    "get_realtime_data": {
        "task": "stock_tasks.stocks.get_realtime_data.run",  #执行的函数
        #"schedule": crontab(minute="*/1"),   # every minute 每分钟执行
        "schedule": timedelta(seconds=2),
        "args": ()  # # 任务函数参数
    },
}
