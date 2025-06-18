# 注册接口测试数据
REGISTER_TEST_DATA = [
    # 有效数据
    {"username": "valid_user", "password": "ValidPass123!", "email": "valid@example.com"},

    # 无效数据
    {"username": "", "password": "ValidPass123!", "email": "empty@example.com"},  # 空用户名
    {"username": "short", "password": "short", "email": "short@example.com"},  # 密码过短
    {"username": "no_password", "password": "", "email": "no_pass@example.com"},  # 空密码
    {"username": "invalid_email", "password": "ValidPass123!", "email": "not_an_email"},  # 无效邮箱
    {"username": "sql_injection", "password": "test' OR '1'='1", "email": "sql@example.com"},  # SQL注入尝试
    {"username": "existing_user", "password": "ValidPass123!", "email": "existing@example.com"},  # 重复用户
    {"username": "long_username", "password": "ValidPass123!", "email": "long_username@example.com"},  # 过长的用户名
]