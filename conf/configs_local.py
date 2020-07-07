# coding:utf8
"""各配置参数-本地开发环境"""

CONFIGS_NAME = __file__

# ini配置文件名
INI_NAME = 'conf.ini'

# 文件上传路径，若为空，则用settings里的
UPLOAD_PATH = ""

# DB
DB_HOST = '10.0.0.236'
DB_PORT = 5432
DB_USER = 'postgres'
DB_PWD = 'postgres'
DB_NAME = 'tms_lucktory_test'
DB_TYPE = 'postgresql'

# redis
REDIS_IP = '127.0.0.1'
REDIS_PWD = ''
REDIS_PORT = 6379
