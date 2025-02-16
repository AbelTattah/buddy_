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
                    r = s.post(f"https://libgen.li/index.php?req={search_keywords}&columns%5B%5D=t&columns%5B%5D=a&columns%5B%5D=s&columns%5B%5D=y&columns%5B%5D=p&columns%5B%5D=i&objects%5B%5D=f&objects%5B%5D=e&objects%5B%5D=s&objects%5B%5D=a&objects%5B%5D=p&objects%5B%5D=w&topics%5B%5D=l&topics%5B%5D=c&topics%5B%5D=f&topics%5B%5D=a&topics%5B%5D=m&topics%5B%5D=r&topics%5B%5D=s&res=100&filesuns=all")
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
                        images.append(f"https://books.ms"+image_route)
                        # Append the download link to the links list
                        links.append(al)  
                    if len(titles) == 0 and len(links) == 0:           
                        return titles, links, images
                    else:
                        cache.setCache(search_keywords, [titles,links,images])
                        return titles, links, images
        
