from bs4 import BeautifulSoup
import requests


def scrape_recipe_urls():
    links = set()
    i = 1
    while True:
        index_url = f"https://thegreatbritishbakeoff.co.uk/recipes/all/page/{i}/?filter%5Bcollection%5D=81&showFilter=false&categoryName=Technical%20bakes&fbclid=IwAR0MGnNLK3f_tNBtIL46n91eY2Q6oFfSKxwB7qCgYVr-PZcO8GwLicstUmc#038;showFilter=false&categoryName=Technical+bakes&fbclid=IwAR0MGnNLK3f_tNBtIL46n91eY2Q6oFfSKxwB7qCgYVr-PZcO8GwLicstUmc"
        soup = BeautifulSoup(requests.get(index_url).content)
        new_links = soup.find_all("a", "recipes-loop__item__link")
        if not new_links:
            break
        links |= set(link.attrs['href'] for link in new_links)
        i += 1
    return links
