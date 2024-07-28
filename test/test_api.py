import pytest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_root_redirect():
    response = client.get("/")
    assert response.status_code == 200
    assert str(response.url).endswith("/docs")

def test_get_assets_valid():
    response = client.post("/assets/", json={"chain_name": "eth-mainnet", "wallet_address": "0x6105f0b07341eE41562fd359Ff705a8698Dd3109"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_assets_missing_chain_name():
    response = client.post("/assets/", json={"chain_name": "", "wallet_address": "0x6105f0b07341eE41562fd359Ff705a8698Dd3109"})
    assert response.status_code == 400
    assert response.json()["detail"] == "chain_name was not provided"

def test_get_total_usd_value_valid():
    response = client.post("/total_usd_value/", json={"chain_name": "eth-mainnet", "wallet_address": "0x6105f0b07341eE41562fd359Ff705a8698Dd3109"})
    assert response.status_code == 200
    data = response.json()
    assert "wallet_address" in data
    assert "total_usd_value" in data
    assert isinstance(data["total_usd_value"], float)

def test_get_transactions_valid():
    response = client.post("/transactions/", json={"chain_name": "eth-mainnet", "wallet_adress": "0x6105f0b07341eE41562fd359Ff705a8698Dd3109"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
