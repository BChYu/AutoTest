import pytest

@pytest.mark.parametrize('a,b,expected',[
    (1,2,3),
    (0,0,0),
    (-1,1,0),
    (100,200,300)
])
def test_addition(a,b,expected):
    '''加法'''
    assert a + b == expected

@pytest.mark.parametrize('a,b,expected_exception',
                         [(10,5,None),
                          (5,0,ZeroDivisionError),
                          ('10',2,TypeError),
                          (-4,-2,None)])
def test_division(a,b,expected_exception):
    '''除法'''
    if expected_exception:
        with pytest.raises(expected_exception):
            a / b
    else:
        assert a / b == 2

