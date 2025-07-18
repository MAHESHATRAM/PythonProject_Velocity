import pytest
@pytest.fixture
def sample_user():
    return{"username":"Rohit","Role":"Dev"}

def test_user_role(sample_user):
    assert sample_user["Role"] == "Dev"
    
def test_user_name(sample_user):
    assert sample_user["username"] == "Rohit1"
    