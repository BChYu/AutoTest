import pymysql
from config.db_config import DB_CONFIG
from pymysql.cursors import DictCursor

#数据库客户端工具类
class DBClient:
    def __init__(self):
        self.connection = pymysql.connect(**DB_CONFIG)                      #连接数据库
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)    #创建数据库游标 字典格式

    def execute_query(self, sql, params=None):
        """执行查询并返回结果"""
        self.cursor.execute(sql, params or ())  #如果params为None，使用空元组替代
        return self.cursor.fetchall()

    def execute_update(self, sql, params=None):
        """执行更新操作（INSERT/UPDATE/DELETE）"""
        affected_rows = self.cursor.execute(sql, params or ())
        self.connection.commit()
        return affected_rows    # 返回影响的行数

    def user_exists(self, username):
        """检查用户名是否存在"""
        sql = "SELECT COUNT(*) AS count FROM users WHERE username = %s"
        result = self.execute_query(sql, (username,))   # [{'count': 1}]  # count=1表示存在
        return result[0]['count'] > 0 if result else False

    def get_user(self, username):
        """获取用户信息"""
        sql = "SELECT * FROM users WHERE username = %s"
        return self.execute_query(sql, (username,))[0] if self.user_exists(username) else None

    def close(self):
        """关闭数据库连接"""
        self.cursor.close()             #先关闭游标
        self.connection.close()         #再关闭连接