# Day1 pytest安装 测试函数编写 assert断言 github提交
## 如何运行测试
1. 安装依赖：`pip install pytest`
2. 执行测试：`pytest -v`

# Day2 参数化测试与Fixture管理
## 1. **Pytest 测试框架**
   - 掌握 `@pytest.fixture` 的使用
   - 学习参数化测试 `@pytest.mark.parametrize`
## 2.创建数据驱动测试

# Day3 API自动化测试实战
## 1.掌握requests库发送HTTP请求
## 2.验证API响应（状态码/JSON/Headers）
## 3.设计可维护的API测试框架结构
## 4.实现数据驱动的API测试

# Day4 API自动化框架搭建：封装请求工具类 + 数据驱动
## 测试抖音开放API（视频列表接口）
## 1.apiclient 基础请求封装
## 2.douyinapi 平台专业接口(满足特定需求)
## 3.测试与实现分离（参数化测试，fixture）
### 无access_token 改用模拟测试
### 添加模拟测试(mocking)
### 使用环境变量管理敏感信息
### 添加日志记录


# Day 5: 数据库验证与pymysql集成测试
## 掌握pymysql库的使用：连接数据库、创建游标、执行查询和处理结果
## 数据库断言：在接口测试后验证数据库中的数据变更
## 测试注册流程：完整的注册API→数据库验证工作流
## 数据清理：测试后的数据库清理操作`yield fixture` 
## DBClient封装、使用环境变量管理敏感凭据、单独存放数据库配置文件

# day 8: Selenium环境搭建
## 编写web自动化脚本
```bash
##UI自动化测试
cd ui_tests/day1_env_setup
python first_selenium_script.py