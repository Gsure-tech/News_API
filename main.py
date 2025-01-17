import requests

url = "060531c83c86433ba1de4c75f99209e5"
request = requests.get(url)
content = request.text
print(content)