import requests


def perform_get_request():
    """Perform GET request to given URL and return the response"""
    url = 'https://httpbin.org/get'
    response = requests.get(url)
    return response


def perform_get_request_with_params():
    """Perform GET request to given URL sending any parameter and return the response"""
    # HINT: you should add the GET parameters at the end of the url
    url = 'https://httpbin.org/get'
    params = {'user': 'rmotr'}
    response = requests.get(url, params=params)
    return response


def perform_post_request():
    """Perform POST request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/post'
    data = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }
    response = requests.post(url, json=data)
    return response


def perform_put_request():
    """Perform PUT request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/put'
    data = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }
    response = requests.put(url, json=data)
    return response


def perform_patch_request():
    """Perform PATCH request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/patch'
    data = {
        'first_name': 'Guido'
    }
    response = requests.patch(url, json=data)
    return response


def perform_delete_request():
    """Perform DELETE request to given URL and return the response"""
    url = 'https://httpbin.org/delete'
    response = requests.delete(url)
    return response


def perform_redirect_request():
    """Perform a request to a redirect URL and return the Location header that come in the response"""
    # HINT: you should use the allow_redirects parameter while doing the request
    url = 'https://httpbin.org/redirect/1'
    params = {'url': 'https://rmotr.com'}
    response = requests.get(url, params=params, allow_redirects=False)
    return response.headers['Location']