import requests
import bs4

# trying to start from the first page
page_num = 1 
current_url = f"http://quotes.toscrape.com/page/{page_num}/"

unique_authors = set()

while True:
    res = requests.get(current_url) 
    soup = bs4.BeautifulSoup(res.text, "lxml")
    authors = soup.select(".author")
    next_button = soup.select(".next")
    
    if next_button:
        for name in authors:
            unique_authors.add(name.text) 
            
        page_num += 1
        current_url = current_url = f"http://quotes.toscrape.com/page/{page_num}/"
    
    else:
        break
    