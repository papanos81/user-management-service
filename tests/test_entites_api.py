from src.model.schemas import UserBase
from src.main import app
from fastapi.testclient import TestClient
import datetime
from pydantic import ValidationError
import pytest
import json

test = TestClient(app)


def test_not_found_user_error():
  response = test.get('/myuser')
  assert response.status_code == 404

def test_create_user():
  user = {
    "username": "smouheb",
    "email": "sma@sma.nl",
    "age": 48
  }
  response = test.post("/user", json=user)
  assert response.status_code == 201

def test_get_users_created():
  response = test.get('/user/smouheb')
  assert response.json()['username'] == 'smouheb'
  assert response.json()['updated_at'] is  None
  assert response.status_code == 200

def test_create_user_without_mandatory_data():
  user = {
    "email": "sma@sma.nl",
    "age": 78
  }
  response = test.post("/user", json=user)
  assert response.status_code == 422

def test_create_user_unique_username():
  user = {
    "username": "smouheb",
    "email": "sma@sma.nl",
    "age": 48
  }
  response = test.post("/user", json=user)
  assert response.status_code == 400

def test_modify_user():
  user = {
    "username": "smouheb",
    "email": "sma@smas.nl",
    "age": 49
  }
  response = test.put("/user", json=user)
  assert response.json()['email'] == 'sma@smas.nl'
  assert response.json()['age'] == 49
  assert response.json()['updated_at'] is not None
  assert response.status_code == 201


def test_modify_user_not_allowed():
  pass

def test_delete_user_by_id():
  user_id = test.get("/user/smouheb").json()
  response = test.delete(f"/user/{user_id['unique_id']}")
  assert response.status_code == 202