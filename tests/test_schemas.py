from src.model.schemas import UserBase
from datetime import datetime
from pydantic import ValidationError
import pytest


def test_user_create_schema():
    user_in = UserBase(id="1234",
                       username="testuser", 
                       email="test@example.com", 
                       age=43, 
                       created_at=datetime.now())
    assert user_in.username == "testuser"
    assert user_in.email == "test@example.com"
    assert user_in.age == 43
    assert isinstance(user_in.created_at, datetime)


def test_user_wrong_type_schema():
    with pytest.raises(ValidationError):
        UserBase(username="testuser", email="test@example.com", age="REO", created_at=datetime.now())

def test_user_missing_mandatory_type_schema():
    with pytest.raises(ValidationError):
        UserBase(username="testuser", email="test@example.com", age="REO")

def test_user_unique_user_id():
    pass