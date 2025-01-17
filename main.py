import requests

api_key = "060531c83c86433ba1de4c75f99209e5"
url =
request = requests.get(url)
content = request.text
print(content)