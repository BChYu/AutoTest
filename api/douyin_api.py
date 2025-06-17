from .api_client import APIClient
import os

class DouyinAPI(APIClient):
    def __init__(self):
        super().__init__("https://open.douyin.com/")
        token = os.getenv('DOUYIN_TOKEN','YOUR_ACCESS_TOKEN')
        self.session.headers.update({
            'Authorization': f'Bearer {token}'                         # 认证令牌
        })

    def get_video_list(self, user_id, page=1, size=20):
        """获取用户视频列表"""
        endpoint = 'platform/video/list/'
        params = {
            'user_id': user_id,
            'page': page,                               # 分页页码
            'size': size                                # 每页数量
        }
        return self.get(endpoint, params)