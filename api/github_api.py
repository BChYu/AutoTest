import pytest
import requests

#编写API封装类
class GitHubAPI:
    def __init__(self):
        self.base_url = 'https://api.github.com'
        self.headers = {
            'Accept': 'application/vnd.github.v3+json'#设置 HTTP 请求头（header） accept指定客户端期望接收的数据格式
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    # def get_user(self, username):
    #     '''获取用户信息'''
    #     url = f'{self.base_url}/users/{username}'
    #     response = requests.get(url, headers = self.headers)
    #     return response
    def get_user(self, username):
        '''获取用户信息'''
        try:
            url = f'{self.base_url}/users/{username}'
            response = self.session.get(url, timeout=5)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            pytest.fail(f'API请求失败：{str(e)}')
    def get_repo(self, owner, repo_name):
        '''获取仓库信息'''
        url = f"{self.base_url}/repos/{owner}/{repo_name}"
        response = requests.get(url, headers = self.headers)
        return response
    def search_repositories(self, query, sort = "stars", order = 'desc'):
        '''搜索仓库'''
        url = f'{self.base_url}/search/repositories'
        params = {'q': query, 'sort': sort, 'order': order}#query: 搜索关键词(如 language:python)
        response = requests.get(url, headers = self.headers, params=params)
        return response #返回HTTP 状态码（如 200 表示成功）和 响应对象，可通过 .json() 解析为字典