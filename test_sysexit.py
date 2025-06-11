import pytest


def f():
    raise SystemExit(1) #定义一个会引发 SystemExit 异常的函数
def test_mytest():
    with pytest.raises(SystemExit):# 使用 pytest 的异常断言上下文 验证代码是否引发预期的异常
        f()# 调用会引发异常的函数

# with pytest.raises(预期异常类型):
#     可能会抛出异常的代码