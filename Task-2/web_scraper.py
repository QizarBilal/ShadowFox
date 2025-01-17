import requests
from bs4 import BeautifulSoup
site = "https://quotes.toscrape.com"
data = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
content = requests.get(site, headers=data)
if content.status_code == 200:
    parsing_web = BeautifulSoup(content.text, 'html.parser')
    print("Extracted Insights:")
    hidden_elements = parsing_web.find_all('span', class_='text') 
    for idx, hidden_data in enumerate(hidden_elements, 1):
        print(f"{idx}. {hidden_data.get_text(strip=True)}")
else:
    print(f"Operation failed with code: {content.status_code}")
