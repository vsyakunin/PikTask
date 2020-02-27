from webapp import create_app
from flask import json

def test_verify(test_client):
    test_data=[
        "Курская"
    ]
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = test_client.post('/api/v1/metro/verificate', headers = headers, data=json.dumps(test_data))
    
    assert response.status_code == 200

def test_verify_mimetype(test_client):
    test_data=[
        "Курская"
    ]
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = test_client.post('/api/v1/metro/verificate', headers = headers, data=json.dumps(test_data))

    assert response.mimetype == 'application/json'
    
def test_verify_unchanged(test_client):
    test_data=[
        "Курская"
    ]
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = test_client.post('/api/v1/metro/verificate', headers = headers, data=json.dumps(test_data))

    assert response.json["unchanged"] == test_data

def test_verify_deleted(test_client):
    test_data=[
        "Курская"
    ]
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = test_client.post('/api/v1/metro/verificate', headers = headers, data=json.dumps(test_data))

    assert response.json["deleted"] != test_data

def test_verify_updated(test_client):
    test_data=[
        "НЕСУЩЕСТВУЮЩАЯ СТАНЦИЯ"
    ]
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = test_client.post('/api/v1/metro/verificate', headers = headers, data=json.dumps(test_data))

    assert response.json["updated"] == test_data    
