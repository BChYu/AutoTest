import requests
import json
import logging

class APIClient:
    def __init__(self, base_url):
        self.logger = logging.getLogger(__name__)   # 添加日志
        self.base_url = base_url                # API基础URL
        self.session = requests.Session()       # 创建持久会话
        self.session.headers = {
            'Content-Type': 'application/json', # 声明发送JSON数据
            'User-Agent': 'AutoTest/1.0'        # 标识客户端身份
        }
    def get(self, endpoint, params=None):
        '''发送GET请求'''
        url = f'{self.base_url}{endpoint}'
        response = self.session.get(url, params=params)
        return self._handle_response(response)  # 统一处理响应

    def post(self, endpoint, data=None):
        '''发送POST请求'''
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=data)
        return  self._handle_response(response)

    def _handle_response(self, response):
        '''统一处理响应'''
        try:
            response.raise_for_status()         # 检查HTTP状态码 (4xx/5xx会触发异常)
            self.logger.info(f'API请求成功： {response.url}')
            return response
        except requests.exceptions.HTTPError as err:
            print(f"HTTP错误：{err}")
            self.logger.error(f'HTTP错误：{err}')
            # return None
            return response  # 仍然返回响应对象（可通过response.status_code获取状态码）
        except json.JSONDecodeError:
            print('响应不是有效的JSON格式')
            # return None
            return response