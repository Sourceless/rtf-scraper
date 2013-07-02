import requests
from BeautifulSoup import BeautifulSoup


def map_site(url):
    '''Find all the linked-to pages of a site and return a list of them'''
    not_searched = [url]
    searched = []

    while len(not_searched):
        # really terrible, O(n^2), but it needs done fast, so...
        search_url = not_searched.pop()
        if search_url not in searched:
            print "Searching {}".format(search_url)
            not_searched.extend(scrape_links(url, search_url))
        else:
            continue # skip, already searched
        searched.append(search_url) 

    return searched


def scrape_links(root, url):
    '''Scrape an url for links, return a list of urls'''
    page = requests.get(url)
    soup = BeautifulSoup(page.text)

    anchors = soup.findAll('a', href=True)
    anchors = [dict(anchor.attrs)['href'] for anchor in anchors]
    anchors = [anchor for anchor in anchors if anchor != None]
    anchors = [rootify(root, anchor) for anchor in anchors if anchor.startswith('/')]

    return anchors


def rootify(root, url):
    if url.startswith(u'/'): # It's a relative path
        return '/'.join(u.strip('/') for u in (root, url))
    return url
