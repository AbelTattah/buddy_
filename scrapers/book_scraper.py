from bs4 import BeautifulSoup
import requests
from store_local import cache_local

title = "Libgen & IPFS & Tor"
"""
TODO: improve format_search_keyword: Done

"""

cache = cache_local.Cache_Local()

class Scrape:
        def __init__(self):
            pass       
        
        def format_search_keyword(self,keyword):
            initial = keyword.split(" ")
            final = ""
            for i in range(0,len(initial)):
                if i == 0:
                    final+=initial[i]
                else:
                    final+="+"+initial[i]
            return final
        
        def scrape(self,search_keywords):
            results = cache.getCache(search_keywords)
            if len(results) == 3:
                return results[0], results[1], results[2]
            else:
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
                        return titles, links, images
                    else:
                        cache.setCache(search_keywords, [titles,links,images])
                        return titles, links, images
        
