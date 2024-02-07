import requests

payload = {'firstName': 'John', 'lastName': 'AlGohary'}
r = requests.get('https://httpbin.org/get', params=payload)

print(r.url)
# print(r.status_code)
# print(r.content)
# print(r.text)

# payload = {'firstName': 'John', 'lastName': 'AlGohary'}
# r = requests.post('https://httpbin.org/post', data=payload)
# print(r.text)


import requests
import sys


def send_a_letter(the_letter):
    if the_letter:
        payload = {"q": the_letter}
    else:
        payload = {"q": ""}
    
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    
    if response.headers['content-type'] == "application/json":
        data = response.json()
        if data:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    else:
        print("Not a valid JSON")











