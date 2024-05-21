from bs4 import BeautifulSoup
import requests

title = "Libgen & IPFS & Tor"
"""
TODO: improve format_search_keyword

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
        r = s.post(f"https://libgen.is/search.php?req={search_keywords}&open=0&res=25&view=simple&phrase=1&column=def")
        titles = []
        links = []
        soup = BeautifulSoup(r.text, 'html.parser')
        for td in soup.find_all('td',width = 500):
            titles.append(td.get_text())
        for link in soup.find_all('a',title=title):
            t = s.post(link.get('href'))
            re = BeautifulSoup(t.text,'html.parser')
            nl = re.find('a')
            al = nl.get('href')
            links.append(al)  
        if len(titles) == 0 and len(links) == 0:  
            titles.append("Not found")
            links.append("Not found")          
            return titles, links
        else:
            return titles, links

