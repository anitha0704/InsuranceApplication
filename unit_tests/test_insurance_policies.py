import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is in main.py

client = TestClient(app)

# Test fetching all policies
def test_get_all_policies():
    response = client.get("/policies/")
    assert response.status_code == 200
    assert "response" in response.json()

# Test searching policies by name
def test_search_policies_by_name():
    response = client.get("/policies/search/?name=Health")
    assert response.status_code == 200
    assert "response" in response.json()

# Test filtering policies with multiple criteria
def test_filter_policies():
    response = client.get("/policies/filter/?policy_type=Health&min_premium=1000&max_premium=5000")
    assert response.status_code == 200
    assert "response" in response.json()

# Test sorting policies
def test_sort_policies():
    response = client.get("/policies/filter/?sort_by_premium=asc")
    assert response.status_code == 200
    assert "response" in response.json()
