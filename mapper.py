import requests
from BeautifulSoup import BeautifulSoup
import os.path

def scrape_links(root, url):
    '''Scrape an url for links, return a list of urls'''
    page = requests.get(url)
    soup = BeautifulSoup(page.text)

    anchors = soup.findAll('a', href=True)
    anchors = [rootify(root, anchor.attrs[0][1]) for anchor in anchors]

    return anchors


def rootify(root, url):
    if url.startswith(u'/'): # It's a relative path
        return '/'.join(u.strip('/') for u in (root, url))
    return url


if __name__ == '__main__':
    print scrape_links("http://www.restorethefourth.net/", "http://www.restorethefourth.net/")

