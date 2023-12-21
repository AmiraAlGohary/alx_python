import requests
r = requests.get('https://alu-intranet.hbtn.io/status')

print("Body response:")
print("\t- type: " + str(type(r.reason)))
print("\t- content: " + r.reason)