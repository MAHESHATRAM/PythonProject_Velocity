import pytest
def test_pass():
    assert 10 + 10 == 20

def test_fail():
    assert 10+10 == 2
    
def test_error():
    raise ValueError("Something went wrong")

@pytest.mark.skip(reason='Future not reply')
def test_skip():
    assert True
    
