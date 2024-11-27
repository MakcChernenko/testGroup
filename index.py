import requests
import bs4

response = requests.get("http://127.0.0.1:8000/")

if response.status_code == 200:
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h1")
    for title in titles:
        print(title.text.strip())