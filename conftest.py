import json
import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def config():
    """读取并验证配置文件"""
    config_path = Path(__file__).parent / "config.json"
    # print(Path(__file__))  # 输出: /home/user/project/conftest.py
    # print(Path(__file__).parent)  # 输出: /home/user/project
    # print(config_path)  # 输出: /home/user/project/config.json
    try:
        with open(config_path) as f:
            config = json.load(f)
    except FileNotFoundError:
        pytest.fail("config.json 文件未找到")
    except json.JSONDecodeError:
        pytest.fail("config.json 格式错误")

    assert "base_url" in config, "配置缺少 base_url"
    assert isinstance(config["timeout"], (int, float)), "timeout 必须是数字"
    return config

# test_api.py
def test_api_config(config):
    assert config["base_url"].startswith("http")
    assert 1 <= config["timeout"] <= 30  # 验证超时范围合理

def test_user(config):
    assert config["test_users"][0] == {'username': 'test_user1', 'role': 'admin'}
