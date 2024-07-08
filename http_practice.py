import requests

# Exercise 1: Perform a simple GET request
def get_request(url):
    response = requests.get(url)
    return response

# Exercise 2: Perform a GET request with parameters
def get_request_with_params(url, params):
    response = requests.get(url, params=params)
    return response

# Exercise 3: Perform a POST request
def post_request(url, data):
    response = requests.post(url, data=data)
    return response

# Exercise 4: Perform a PUT request
def put_request(url, data):
    response = requests.put(url, data=data)
    return response

# Exercise 5: Perform a PATCH request
def patch_request(url, data):
    response = requests.patch(url, data=data)
    return response

# Exercise 6: Perform a DELETE request
def delete_request(url):
    response = requests.delete(url)
    return response

# Exercise 7: Inspect headers during a redirect request
def get_redirect_location(url):
    response = requests.get(url, allow_redirects=False)
    if response.status_code in [301, 302, 303, 307, 308]:  # Redirection status codes
        location = response.headers.get('Location')
        return location
    return None

# Main function for testing manually if needed
if __name__ == "__main__":
    url = 'https://example.com'
    
    print("1. Performing a simple GET request:")
    print(get_request(url))
    
    print("\n2. Performing a GET request with parameters:")
    params = {'q': 'python language'}
    print(get_request_with_params('https://www.google.com/search', params))
    
    print("\n3. Performing a POST request:")
    data = {'key': 'value'}
    print(post_request(url, data))
    
    print("\n4. Performing a PUT request:")
    print(put_request(url, data))
    
    print("\n5. Performing a PATCH request:")
    print(patch_request(url, data))
    
    print("\n6. Performing a DELETE request:")
    print(delete_request(url))
    
    print("\n7. Inspecting headers during a redirect request:")
    redirect_url = 'http://httpbin.org/redirect-to?url=https://example.com'
    print(get_redirect_location(redirect_url))
