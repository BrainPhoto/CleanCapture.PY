import pytest
import requests
from unittest.mock import patch
from app import PREDICTION_KEY, URL_ENDPOINT_IMAGE, URL_ENDPOINT_URL  

@pytest.fixture
def mock_image_response():
    return {
        "predictions": [
            {"tagName": "plastic", "probability": 0.95},
            {"tagName": "organic", "probability": 0.05}
        ]
    }

@patch('requests.post')
def test_predict_image(mock_post, mock_image_response):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = mock_image_response

    # Test for image upload functionality
    response = requests.post(URL_ENDPOINT_IMAGE, headers={
        "Prediction-Key": PREDICTION_KEY,
        "Content-Type": "application/octet-stream"
    }, data=b'some-image-data')

    assert response.status_code == 200
    assert response.json() == mock_image_response
    predictions = response.json()["predictions"]
    assert len(predictions) == 2
    assert predictions[0]["tagName"] == "plastic"
    assert predictions[0]["probability"] == 0.95

@patch('requests.post')
def test_predict_image_url(mock_post, mock_image_response):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = mock_image_response

    # Test for image URL functionality
    response = requests.post(URL_ENDPOINT_URL, headers={
        "Prediction-Key": PREDICTION_KEY,
        "Content-Type": "application/json"
    }, json={"Url": "http://example.com/image.png"})

    assert response.status_code == 200
    assert response.json() == mock_image_response
    predictions = response.json()["predictions"]
    assert len(predictions) == 2
    assert predictions[0]["tagName"] == "plastic"
    assert predictions[0]["probability"] == 0.95
