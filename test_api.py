
# tests/test_api.py

import requests

BASE_URL = "http://localhost:8000"

def test_health_check():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "status" in response.json()

def test_predict_valid_input():
    sample_features = {
        "features": [0.1] * 20  # Replace with realistic test vector
    }
    response = requests.post(f"{BASE_URL}/predict", json=sample_features)
    assert response.status_code == 200
    assert "prediction" in response.json()
