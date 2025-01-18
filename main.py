import requests
from send_email import send_email

api_key = "060531c83c86433ba1de4c75f99209e5"
url =("https://newsapi.org/v2/everything?q=tesla&from="
      "2024-12-18&sortBy=publishedAt&apiKey="
      "060531c83c86433ba1de4c75f99209e5")

# Male request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
# print(content)

# # Access the article titles and description
for article in content["articles"]:
    topic = article["title"]
    desc = article["description"]
    message = topic + " \n" + desc
    send_email(message)
    # message = f"{article["title"]} {article["description"]}"
    # send_email(message)
#     print(article["title"])
#     print(article["description"])
