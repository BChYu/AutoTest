import pytest
@pytest.mark.parametrize('a,b,c', [
    (1,2,3),
    (5,2,7),
    (3,6,9)
])
def test_addition(a,b,c):
    '''加法'''
    assert a+b == c

@pytest.mark.parametrize('a,b,c', [
    (5,3,2),
    (9,6,3),
    (6,0,6)
])
def test_subtraction(a,b,c):
    '''减法'''
    result = a-b
    assert result == c

def test_string_concatenation():
    assert "hello" + "world" == "helloworld"

def test_list_length():
    fruits = ["apple", "banana"]
    assert len(fruits) == 2

def test_zero_division():
    with pytest.raises(ZeroDivisionError):  # 断言会抛出特定异常
        1 / 0  # 触发除零错误

def test_failure_message():
    # 当失败时显示自定义错误信息（扩展学习）
    result = 9
    assert result % 2 == 1, f"{result}是偶数，但测试要求奇数"

def f():
    raise SystemExit(1) #定义一个会引发 SystemExit 异常的函数
def test_mytest():
    with pytest.raises(SystemExit):# 使用 pytest 的异常断言上下文 验证代码是否引发预期的异常
        f()# 调用会引发异常的函数

def test_file_operations(tmp_path):#文件读写测试
    tmp_file = tmp_path / 'test_file.txt'
    content = 'Hello pytest!'
    tmp_file.write_text(content)
    assert tmp_file.exists()
    assert tmp_file.read_text() == content

# pytest
# pytest -v