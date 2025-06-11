import pytest
from task_04_flask import app



@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask API!" in response.data

def test_data(client):
    response = client.get('/data')
    assert response.status_code == 200
    assert response.get_json() == ["jane", "john"]

def test_status(client):
    response = client.get('/status')
    assert response.status_code == 200
    assert response.data == b"OK"

def test_get_user_jane(client):
    response = client.get('/users/jane')
    assert response.status_code == 200
    assert response.get_json() == {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }

def test_get_user_not_found(client):
    response = client.get('/users/doesnotexist')
    assert response.status_code == 404
    assert response.get_json() == {"error": "User not found"}

def test_add_user(client):
    new_user = {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "Paris"
    }
    response = client.post('/add_user', json=new_user)
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "User added"
    assert data["user"] == new_user
    