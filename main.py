import requests
from send_email import send_email

api_key = "060531c83c86433ba1de4c75f99209e5"
url =("https://newsapi.org/v2/everything?q=tesla&from=2024-12-17&"
      "sortBy=publishedAt&apiKey="
      "060531c83c86433ba1de4c75f99209e5")
request = requests.get(url)
content = request.json()
for article in content["articles"]:
    message = f"{article['title']} {article['description']}"
    send_email(message)
    # print(article["title"])
    # print(article["description"])
