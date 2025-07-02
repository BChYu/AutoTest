import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.add_argument("--disable-blink-features=Automation")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("user-agent=124.0.0.0")

service = Service('/home/ybc/chromedriver-linux64/chromedriver')
driver = webdriver.Chrome(service=service,options=options)

try:
    print('打开京东首页')
    driver.get('https://www.jd.com')
    search_box = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, 'key'))
    )
    search_box.send_keys('3000以上智能手机' + Keys.RETURN)
    print('已搜索关键词：智能手机')
    # ------ 核心技巧：处理动态加载商品列表 ------
    print("\n===== 处理动态加载商品 =====")
    # 1. 等待搜索结果容器出现
    # element = driver.find_element(By.CSS_SELECTOR, "[class^='tbpc-row']")
    # print("元素已存在，选择器正确")
    WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#J_goodsList")) # why 只有这种方式可以，id不可以 因为动态
    )
    print('商品列表容器已加载')
    # 2. 等待首个商品元素可见且可交互
    first_item = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR,"a[onclick*='0']"))
    )
    print('首件商品元素已可见')
    # 3. 等待商品价格加载完成
    WebDriverWait(driver,15).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR,"[data-price]")
        )
    )
    print('商品价格已加载')
    # 4. 滚动到页面底部触发更多商品加载
    initial_items = driver.find_elements(By.CSS_SELECTOR, "div#J_goodsList ul.gl-warp li.gl-item")
    print(f"初始商品数量: {len(initial_items)}")
    print('滚动页面触发加载...')
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    #document.body.scrollHeight 表示整个文档（包括未显示部分）的总高度
    for i in range(1):
        scroll_to = (i + 1) * 0.1 * driver.execute_script("return document.body.scrollHeight")
        driver.execute_script(f"window.scrollTo(0,{scroll_to});")
        wait_time = random.uniform(1.0, 2.0)
        print(f"滚动到{round((i+1)*10)}%位置，等待{wait_time:.1f}秒")
        time.sleep(wait_time)
    #动态等待关键
    # WebDriverWait(driver, 20).until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "div#J_goodsList li.gl-item")) > len(initial_items)) # 正常需要这一行，但反爬无法执行
    new_items = driver.find_elements(By.CSS_SELECTOR, "div#J_goodsList li.gl-item")
    print(f"新商品已加载! 当前商品总数: {len(new_items)}")  #jd的反爬 无法实现

    # ------ 提取商品数据 ------
    print("\n===== 提取商品信息 =====")
    items = driver.find_elements(By.CSS_SELECTOR, "li.gl-item")
    for i, item in enumerate(items[:5], 1):
        # title = item.find_element(By.CSS_SELECTOR, "[class*='p-name']").text.strip()
        #只提取商品名称
        product_name = item.find_element(By.CSS_SELECTOR, "[class*='p-name'] a em").text.strip()

        price = item.find_element(By.CSS_SELECTOR, "i[data-price]").text
        promo_info = []
        try:
            promo_container = item.find_element(By.CSS_SELECTOR, "div.p-icons")
            promo_tags = promo_container.find_elements(By.CSS_SELECTOR, "i[class*=goods-icons4]")
            for tag in promo_tags:
                promo_text = tag.text.strip()
                promo_detail = tag.get_attribute('data-tips')   #   .J-picon-tips 类 - 表示有悬停提示功能
                if promo_detail and promo_detail not in promo_text:
                    promo_text += f"({promo_detail})"
                promo_info.append(promo_text)
        except:
            promo_info.append("无促销")
        if not promo_info:
            promo_info.append("无促销")
        promo_display = " | ".join(promo_info)
        print(f"{i}. {product_name}")
        print(f"   价格: ¥{price} | 促销: {promo_display}")
        print("-" * 60)
    print("任务完成！成功处理动态加载页面")

finally:
    driver.quit()
    print('浏览器已关闭')