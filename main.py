import requests
from send_email import send_email

api_key = "060531c83c86433ba1de4c75f99209e5"
url =("https://newsapi.org/v2/top-headlines?"
      "sources=techcrunch&"
      "apiKey=060531c83c86433ba1de4c75f99209e5&"
      "language=en")

# Male request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
# print(content)

# # Access the article titles and description
body = ""
for article in content["articles"][:5]:
    if article["title"] is not None:
        body = ("Subject: Today's news"
                + "\n" + body + article["title"]
                + "\n"+ article["description"]
                + "\n" + article["url"] + 2*"\n")

body = body.encode("utf-8")
send_email(message=body)
