import pytest


@pytest.fixture
def user_data():
    return {'username': 'test_user', 'password': 'ybc123456'}
def test_login(user_data):
    assert len(user_data['password']) >= 8

@pytest.fixture(scope="session")
def database_connection():
    print('\n=== 创建数据库连接 ===')
    conn = '模拟的数据库连接'
    yield conn
    print('\n=== 关闭数据库连接 ===')
def test_db_query(database_connection):
    assert '连接' in database_connection