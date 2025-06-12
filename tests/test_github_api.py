import pytest
from api.github_api import GitHubAPI
from api.test_data import TEST_USERS, TEST_REPOSITORIES, SEARCH_QUERIES
from test_fixtures import user_data


@pytest.fixture(scope="module")
def api_client():
    return GitHubAPI()  # 模块级fixture复用API客户端

class TestGitHubAPI:
    @pytest.mark.parametrize('username',TEST_USERS)
    def test_get_user(self,api_client,username):
        '''测试获取用户信息'''
        response = api_client.get_user(username)

        # 验证响应状态码
        assert response.status_code == 200
        # 验证响应内容
        user_data = response.json()
        # print(user_data)
        assert user_data['login'] == username
        assert user_data['id'] > 0
        assert 'avatar_url' in user_data

    @pytest.mark.parametrize('owner,repo',TEST_REPOSITORIES)
    def test_get_repository(self,api_client,owner,repo):
        """测试获取仓库信息"""
        response = api_client.get_repo(owner,repo)

        assert response.status_code == 200
        repo_data = response.json()
        # print(repo_data)
        assert repo_data['name'] == repo
        assert repo_data['owner']['login'] == owner
        assert repo_data['stargazers_count'] > 1000

    @pytest.mark.parametrize('query,num', SEARCH_QUERIES)
    def test_search_queries(self,api_client,query,num):
        """测试仓库搜索功能"""
        response = api_client.search_repositories(query)

        assert response.status_code == 200
        search_data = response.json()
        # print(search_data)
        assert search_data['total_count'] >= num
        assert len(search_data['items']) > 0
        stars = [item['stargazers_count'] for item in search_data['items']]
        assert stars == sorted(stars,reverse=True)#降序

    def test_rate_limit(self,api_client):
        """测试API速率限制"""
        response = api_client.get_user('octocat')
        headers = response.headers
        print(headers)
        # 验证速率限制头信息存在
        assert 'X-RateLimit-Limit' in headers
        assert "X-RateLimit-Used" in headers
        assert "X-RateLimit-Remaining" in headers
        # 验证剩余请求次数为正数
        assert int(headers["X-RateLimit-Remaining"]) > 0

    def test_response_time(self, api_client):
        """验证API响应时间在合理范围内"""
        import time

        start_time = time.time()                    #返回当前时间戳（单位：秒）
        response = api_client.get_user('octocat')
        elpased = time.time() - start_time          #用当前时间减去开始时间

        # 验证响应时间小于1秒
        assert elpased < 1.0
        # 使用requests内置计时器验证
        assert response.elapsed.total_seconds() < 1.0   #.total_seconds() 转换为秒数

    def test_invalid_user(self, api_client):
        """测试获取不存在的用户"""
        response = api_client.get_user('this_user_does_not_exist_12345')
        assert response.status_code == 404

        error_data = response.json()
        assert error_data['message'] == 'Not Found'




