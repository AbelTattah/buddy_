from typing import List
from store_local import cache_local
from scrapers import book_scraper


books = book_scraper.Scrape
cache = cache_local.Cache_Local()

def test_availability():
    assert type(cache.getCache("Book")) == str

def test_saving():
    assert type(cache.setCache("Book",[["helloo"],["123"],["Hi"]])) == str

def test_retrieval():
    assert type(cache.getCache("Book")) == List

if __name__ == "__main__":
    print("All tests passed!")