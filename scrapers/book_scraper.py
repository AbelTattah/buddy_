from bs4 import BeautifulSoup
import requests

title = "Libgen & IPFS & Tor"
"""
TODO: improve format_search_keyword: Done

"""

def format_search_keyword(keyword):
    initial = keyword.split(" ")
    final = ""
    for i in range(0,len(initial)):
        if i == 0:
            final+=initial[i]
        else:
            final+="+"+initial[i]
    return final

def scrape(search_keywords):
    with requests.session() as s:
        # Make a request to the libgen search page
        r = s.post(f"https://libgen.is/search.php?req={search_keywords}&open=0&res=25&view=simple&phrase=1&column=def")
        titles = []
        links = []
        images = []
        soup = BeautifulSoup(r.text, 'html.parser')
        # Extract titles from the search results
        for td in soup.find_all('td',width = 500):
            # Append the title to the titles list
            titles.append(td.get_text())
        for link in soup.find_all('a',title=title):
            # Navigate to the book download page
            t = s.post(link.get('href'))
            # Extract the download link
            re = BeautifulSoup(t.text,'html.parser')
            nl = re.find('a')
            al = nl.get('href')
            image = re.find('img')
            image_route = image.get('src')
            images.append(f"https://library.lol"+image_route)
            # Append the download link to the links list
            links.append(al)  
        if len(titles) == 0 and len(links) == 0:  
            titles.append("Book is not available")
            links.append("Book is not available")          
            return titles, links
        else:
            return titles, links, images

