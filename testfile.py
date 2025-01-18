import requests

# url = "https://finance.yahoo.com"
url ="https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Siam_lilacpoint.jpg/294px-Siam_lilacpoint.jpg"

# request = requests.get(url)
# content = request.text
# print(content)

response = requests.get(url)

with open("image.jpg","wb") as file:
    file.write(response.content)