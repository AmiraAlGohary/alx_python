import requests
import sys

def display_response_body(url):
    response = requests.get(url)
    print(response.text)

    if response.status_code >= 400:
        print("Error code: " + str(response.status_code))

url = sys.argv[1]

display_response_body(url)