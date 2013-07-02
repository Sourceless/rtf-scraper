import mapper
import os
import sys
from collection import defaultdict


def scrape_recursively(url, dir_=os.getcwd()):
    print "Scraping links {}, this could take some time...".format(url)
    link_list = mapper.map_site(url)
    print "Done, mapping..."
    link_list = [link.strip(url) for link in link_list]

    link_map = defaultdict



if __name__ == '__main__':
    scrape_recursively("http://www.restorethefourth.net/") 
