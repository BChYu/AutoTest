from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #浏览器控制实例

try:
    driver.get("https://www.baidu.com")
    print("已成功打开百度首页")

    search_box = driver.find_element(By.ID, 'kw')       #  定位搜索框 'kw'：百度搜索框的 HTML ID
    search_box.send_keys('测试开发')
    print("已输入搜索关键词：测试开发")

    search_box.send_keys(Keys.RETURN)
    print("已执行搜索操作")
    #上述操作等价于
    # search_box.send_keys('测试开发'+ Keys.RETURN)

    # driver.implicitly_wait(3)       #   隐式等待 等待3秒查看结果 作用于find_element 不会影响页面加载
    WebDriverWait(driver, 10).until(EC.title_contains('测试开发'))  #显式等待这 行代码会使整个线程暂停执行，直到条件满足

    print(driver.title)
    assert '测试开发' in driver.title
    print("验证成功：搜索结果页面标题包含'测试开发'")

    first_result = driver.find_element(By.CSS_SELECTOR, '#content_left h3 a')
    print(f'第一条搜索结果：{first_result.text}')
    #       获取 第N条结果
    # all_results = driver.find_elements(By.CSS_SELECTOR, '#content_left h3 a')
    # n = 2  # 获取第2条结果
    # if len(all_results) >= n:
    #     print(all_results[n - 1].text)  # 输出：第二条结果
    # else:
    #     print("没有足够的搜索结果")

finally:
    driver.quit()
    print('浏览器已关闭')

#运行脚本
# python first_selenium_script.py

# 简写
# from contextlib import closing
# with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
#     driver.get("https://www.baidu.com")
#     print("已成功打开百度首页")
#     search_box = driver.find_element(By.ID, 'kw')
#     search_box.send_keys('测试开发' + Keys.RETURN)
#     print("已执行搜索操作")
#     WebDriverWait(driver, 10).until(EC.title_contains('测试开发'))
#     print(f"当前标题: {driver.title}")
#     assert '测试开发' in driver.title
#     print("验证成功：搜索结果页面标题包含'测试开发'")
#     first_result = driver.find_element(By.CSS_SELECTOR, '#content_left h3 a')
#     print(f'第一条搜索结果：{first_result.text}')
# print('浏览器已关闭')