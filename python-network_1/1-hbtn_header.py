import requests
import sys

def get_request_id(url):
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
    return request_id

url = sys.argv[1]
    
get_request_id(url)