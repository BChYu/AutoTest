import json
import pytest
import requests
from api.api_client import APIClient
from unittest.mock import MagicMock


print("\n" + "="*50)
print("CONFTEST.PY IS LOADED!")
print("="*50 + "\n")

@pytest.fixture
def mock_douyin(monkeypatch):
    """模拟抖音API响应"""
    original_handle = APIClient._handle_response
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.status_code = 200
                # 修正为抖音API实际返回的数据结构
                self.json_data = {
                    'status': 200,
                    'message': 'success',
                    'data': {
                        'items': [
                            {'id': 'video1', 'title': 'Test Video 1'},
                            {'id': 'video2', 'title': 'Test Video 2'}
                        ]
                    }
                }
            def json(self):
                return self.json_data
        return MockResponse()
    def mock_handle_response(self, response):
        return mock_get().json_data
    monkeypatch.setattr(requests.Session, 'get', mock_get)
    monkeypatch.setattr(APIClient, '_handle_response', mock_handle_response)
    yield   #恢复原始方法
    monkeypatch.setattr(requests.Session, 'get', requests.Session.get)
    monkeypatch.setattr(APIClient, '_handle_response', original_handle)



