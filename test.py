import requests

req = requests.get("https://google.com")
print(req.status_code)
print(req.text)
