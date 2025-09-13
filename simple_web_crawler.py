import requests
from bs4 import BeautifulSoup
import urllib.parse

def simple_crawler(seed_url):
    """
    A simple web crawler thats fetches a page , extract data all links and prints them.
    """
    try:

        headers = {
            'User-Agent': 'MysimpleCrawler/1.0 (raghavgautam9354@gmail.com)'
        }
        response = requests.get(seed_url , headers=headers , timeout=10)

        response.raise_for_status()
        print(f"Successfully fetched {seed_url}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching{seed_url}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a')

    print(f"\nFound{len(links)} links on the page :\n")


    for link in links:
        href = link.get('href')
        if href:
            complete_url = urllib.parse.urljoin(seed_url , href)
            print(f"Link test : {link.text.strip} ---> Url: {complete_url}")

if __name__ == "__main__":
    start_url = "https://en.wikipedia.org/wiki/World_War_II"
    simple_crawler(start_url)