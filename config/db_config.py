from dotenv import load_dotenv
import os
load_dotenv()

# 数据库配置
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),              #数据库服务器地址
    'port': int(os.getenv('DB_PORT', 3306)),                #服务器端口（MySQL 默认为3306）
    'user': os.getenv('DB_USER', 'test_user'),              #登录用户名
    'password': os.getenv('DB_PASSWORD', 'test_password'),  #登录密码
    'database': os.getenv('DB_NAME', 'test_db'),            #要连接的数据库名称
    'charset': 'utf8mb4'                                    #字符编码
}