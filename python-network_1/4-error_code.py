import requests
import sys

def get_something(url):
    response = requests.get(url)
    the_body = response.content
    if response.status_code >= 400:
        print("Error code: " + str(response.status_code))
    else:
        return the_body

url = sys.argv[1]

get_something(url)