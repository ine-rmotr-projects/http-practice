import pytest
from http_practice import *

# Mock URLs for testing
test_url = 'https://example.com'

# Exercise 1: Test simple GET request
def test_get_request():
    response = get_request(test_url)
    assert response.status_code == 200
    assert response.url == test_url

# Exercise 2: Test GET request with parameters
def test_get_request_with_params():
    params = {'q': 'python language'}
    response = get_request_with_params('https://www.google.com/search', params)
    assert response.status_code == 200
    assert 'python language' in response.url

# Exercise 3: Test POST request
def test_post_request():
    data = {'key': 'value'}
    response = post_request(test_url, data)
    assert response.status_code == 200

# Exercise 4: Test PUT request
def test_put_request():
    data = {'key': 'value'}
    response = put_request(test_url, data)
    assert response.status_code == 200

# Exercise 5: Test PATCH request
def test_patch_request():
    data = {'key': 'value'}
    response = patch_request(test_url, data)
    assert response.status_code == 200

# Exercise 6: Test DELETE request
def test_delete_request():
    response = delete_request(test_url)
    assert response.status_code == 200

# Exercise 7: Test inspecting headers during a redirect request
def test_get_redirect_location():
    redirect_url = 'http://httpbin.org/redirect-to?url=https://example.com'
    location = get_redirect_location(redirect_url)
    assert location == 'https://example.com'

# Running the tests
if __name__ == "__main__":
    pytest.main()
