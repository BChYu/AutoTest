import pytest
from test_data import LOGIN_TEST_DATA

def validate_login(username, password):
    '''模拟登录验证函数'''
    return  username == 'admin' and password == 'secret'

@pytest.mark.parametrize('username, password, expected', LOGIN_TEST_DATA)
def test_login_validation(username, password, expected):
    assert validate_login(username, password) == expected