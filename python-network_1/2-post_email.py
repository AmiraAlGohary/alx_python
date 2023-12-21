import requests
import sys

def send_post_request(url, email):
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print("Your email is: " + str(response.text))


url = sys.argv[1]
email = sys.argv[2]

send_post_request(url, email)