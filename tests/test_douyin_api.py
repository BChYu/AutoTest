import pytest
from api.api_client import APIClient
from test_data.douyin_data import TEST_VIDEO_LIST_DATA
from api.douyin_api import DouyinAPI

# # 抖音API基础URL（使用公开测试API）
# DOUYIN_BASE_URL = "https://www.example.com/api/douyin/"
#
# @pytest.fixture(scope="module")
# def api_client():
#     """创建API客户端"""
#     return APIClient(DOUYIN_BASE_URL)
#
# @pytest.mark.parametrize('test_data', TEST_VIDEO_LIST_DATA)
# def test_video_list(api_client,test_data):
#     """测试获取用户视频列表API"""
#     # 构造API端点
#     endpoint = f'/video/list/?user_id={test_data["user_id"]}'
#
#     # 发送API请求
#     response_data = api_client.get(endpoint)
#
#     #验证响应数量
#     assert response_data is not None
#     assert  'videos' in response_data
#
#     videos = response_data['videos']
#
#     #验证视频数量
#     assert  len(videos) >= test_data['expected_video_count']
#     #验证每个视频的基本信息
#     for video in videos:
#         assert 'title' in video
#         assert 'play_url' in video
#         assert 'likes' in video
#         assert video['likes'] >= test_data['min_likes']
@pytest.fixture(scope="module")
def douyin_client():
    """创建抖音API客户端"""
    return DouyinAPI()


@pytest.mark.parametrize("test_data", TEST_VIDEO_LIST_DATA)
def test_video_list(douyin_client, test_data):
    """测试获取用户视频列表API"""
    response_data = douyin_client.get_video_list(
        user_id=test_data["user_id"]
    )
    print('response_data:{response_data}')
    # 验证响应数据
    assert response_data is not None            # 响应不应为空
    assert "items" in response_data             # 应包含视频列表字段

    videos = response_data["items"]

    # 验证视频数量
    assert len(videos) >= test_data["expected_video_count"]

    # 验证每个视频的基本信息
    for video in videos:
        assert video["statistics"]["like_count"] >= test_data["min_likes"]
