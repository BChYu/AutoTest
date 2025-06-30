from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service=Service('/home/ybc/chromedriver-linux64/chromedriver')
#初始化浏览器
# driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version='138.0.7204.49').install()))
driver = webdriver.Chrome(service=service)
try:
    driver.get('http://www.jd.com')
    driver.maximize_window()
    print('已打开京东首页')
    time.sleep(2)
    # ------ 任务1：定位搜索框（多种方式） ------
    print("\n===== 搜索框定位演示 =====")
    # 方式1：ID定位（最佳选择）
    search_id = driver.find_element(By.ID,'key')
    search_id.send_keys('ID定位成功')
    print('ID定位成功')
    time.sleep(1)
    search_id.clear()
    #方式2：ClassName定位
    search_class = driver.find_element(By.CLASS_NAME,'text')#class属性
    search_class.send_keys('ClassName定位成功')
    print('ClassName定位成功')
    time.sleep(1)
    search_class.clear()
    # 方式3：Name定位 jd无
    # search_name = driver.find_element(By.NAME,'w')
    # search_name.send_keys('Name定位成功')
    # print('Name定位成功')
    # time.sleep(1)
    # search_name.clear()
    # 方式4：XPath定位（绝对路径）
    search_xpath = driver.find_element(By.XPATH,'//*[@id="key"]')#（匹配 id="key" 的任意元素）
    search_xpath.send_keys('XPath定位成功')
    print('XPath定位成功')
    time.sleep(1)
    search_xpath.clear()
    # 方式5：CSS Selector定位
    search_css = driver.find_element(By.CSS_SELECTOR,'input#key')
    search_css.send_keys("CSS定位成功")
    print("CSS定位成功")
    time.sleep(1)
    search_css.clear()

    # ------ 任务2：定位登录按钮 ------
    print("\n===== 登录按钮定位演示 =====")
    # 方式1：LinkText（精确文本）
    login_linktext = driver.find_element(By.LINK_TEXT, '你好，请登录')
    login_linktext.click()
    print("LinkText定位成功 - 点击登录按钮")
    time.sleep(2)
    #返回首页
    driver.back()
    time.sleep(1)
    # 方式2：PartialLinkText（模糊匹配）
    login_partial = driver.find_element(By.PARTIAL_LINK_TEXT,'请登录')
    print('PartialLinkText定位成功')
    #方式3：ClassName + TagName组合
    login_class = driver.find_element(By.CSS_SELECTOR, 'a.link-login')
    print('ClassName + TagName组合定位成功')

    # ------ 任务3：层级定位 ------
    print("\n===== 层级定位演示 =====")
    # # 先定位父元素再定位子元素
    # cart_wrapper = driver.find_element(By.CLASS_NAME, "carts-icon")
    # cart_icon = cart_wrapper.find_element(By.TAG_NAME,'i')
    # # 鼠标悬停在购物车图标上
    # webdriver.ActionChains(driver).move_to_element(cart_icon).perform()
    # print('层级定位成功 - 鼠标悬停在购物车图标上')
    # time.sleep(2)
    #我的京东
    cart_wrapper = driver.find_element(By.CSS_SELECTOR, '#ttbar-myjd > div.dt.cw-icon > a')
    webdriver.ActionChains(driver).move_to_element(cart_wrapper).perform()
    print('鼠标悬停在我的京东')
    time.sleep(2)
    print("所有定位方式演示完成！")
finally:
    driver.quit()
    print('浏览器已关闭')