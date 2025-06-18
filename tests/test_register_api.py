import pytest
import random
import string
import time
from api.api_client import APIClient
from db.db_client import DBClient
from test_data.user_data import REGISTER_TEST_DATA


# 生成用户名
def generate_random_username(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))    #小写字母字符串


@pytest.fixture(scope="module")
def api_client():
    return APIClient(base_url="https://api.your-service.com")   ## HTTP/HTTPS协议


@pytest.fixture(scope="function")
def db_client():
    client = DBClient()
    yield client
    client.close()


def register_user(api_client, user_data):               #用户注册
    return api_client.post("/register", json=user_data)

@pytest.fixture(scope="function")
def test_user(api_client, db_client):
    """创建测试用户并在测试后清理"""
    # 生成用户名
    username = f"test_{generate_random_username()}_{int(time.time())}"
    email = f"{username}@example.com"

    # 注册请求数据
    user_data = {
        "username": username,
        "password": "TestPassword123!",
        "email": email
    }

    # 执行注册请求
    response = register_user(api_client, user_data)

    # 返回用户信息和清理函数
    user_data['api_response'] = response        #   "api_response": response  # 存储注册响应
    yield user_data

    # 测试后清理
    if db_client.user_exists(username):
        db_client.execute_update("DELETE FROM users WHERE username = %s", (username,))


def test_successful_registration(api_client, test_user, db_client):
    """测试成功注册后的数据库验证"""
    # 获取注册响应
    response = test_user['api_response']

    #验证api响应
    assert response.status_code == 200
    assert 'success' in response.json().get('status', '')
    # assert 'success' in response        #其实不需要，在apiclient已经统一处理
    # 验证数据库
    username = test_user['username']
    assert db_client.user_exists(username), "用户应存在于数据库中"

    user_record = db_client.get_user(username)
    assert user_record is not None
    assert user_record['email'] == test_user['email']
    assert user_record['status'] == 'active'  # 按需


# 参数化测试错误注册情况
@pytest.mark.parametrize("user_data", REGISTER_TEST_DATA)
def test_registration_errors(api_client, db_client, user_data):
    """测试各种错误注册情况"""
    if 'username' not in user_data or not user_data['username']:    #缺少 username 字段，或 username 为空
        user_data = user_data.copy()
        user_data['username'] = f"test_error_{generate_random_username()}_{int(time.time())}"

    # 执行注册请求
    response = register_user(api_client, user_data)

    # 验证API响应
    assert response.status_code != 200, "错误注册应返回非200状态码"

    # 验证数据库不应有该用户
    username = user_data.get('username')
    if username:
        assert not db_client.user_exists(username), "错误注册不应创建用户记录"

    # 如果有返回错误信息，验证响应结构
    error_data = response.json()
    assert 'error_code' in error_data
    assert 'message' in error_data