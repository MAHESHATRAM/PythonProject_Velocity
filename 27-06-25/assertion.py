
import pytest
def test_true_condition():
    assert 2+2 ==4
    
def test_string_conditon():
    assert 'a' in 'apple' 
    
def test_list_equality():
    if [1,2,3] == [1,2,3]:
        print(True)
        print('Test case is pass')
    
def test_value_not_equalto():
    assert 5 != 10 
    
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divmod(10,0)
def test_string_match():
   assert "hello".upper() == "HELLO" 
