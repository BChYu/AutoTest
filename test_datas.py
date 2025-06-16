#测试数据集
LOGIN_TEST_DATA = [
    ('admin', 'secret', True),      # 正确凭证
    ('guest', 'pass123', False),    # 错误密码
    ('', 'emptyuser', False)        # 空用户名
]