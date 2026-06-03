import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

headlines = []

for heading in soup.find_all(["h2", "h3"]):
    text = heading.get_text(strip=True)

    if text and text not in headlines:
        headlines.append(text)

with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in headlines[:20]:
        file.write(headline + "\n")

print("Headlines saved successfully!")