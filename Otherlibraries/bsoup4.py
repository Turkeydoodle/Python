from bs4 import BeautifulSoup
import requests
response = requests.get("https://www.piday.org/million/")
soup = BeautifulSoup(response.text, 'html.parser')
for text in soup.stripped_strings:
    print(text)