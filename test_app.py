import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api"

def test_hello():
    response = requests.get(f"{BASE_URL}/hello")
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, World!'}

def test_goodbye():
    response = requests.get(f"{BASE_URL}/goodbye")
    assert response.status_code == 200
    assert response.json() == {'message': 'Goodbye, World!'}
