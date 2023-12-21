import requests
import sys

def search_user(the_letter):
    if the_letter:
        payload = {"q": the_letter}
    else:
        payload = {"q": ""}

    reponse = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    if reponse.headers['content-type'] == 'application/json':
        data = reponse.json()
        if data:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    else:
        print("Not a valid JSON")

if len(sys.argv) == 2:
    the_letter = sys.argv[1]
else:
    the_letter = ""

search_user(the_letter)