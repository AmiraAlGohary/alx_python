import requests
import sys


def get_github_id(username, password):
    url = f"https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    user_data = response.json()
    return user_data["id"]

username = sys.argv[1]
password = sys.argv[2]

get_github_id(username, password)
