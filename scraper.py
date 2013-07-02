import mapper
import requests
import os
import os.path
import sys
import json
import codecs


def scrape_recursively(url, dir_=os.getcwd()):
    print "Scraping links {}, this could take some time...".format(url)
    link_list = mapper.map_site(url)
    print "Done. Scraping pages, this will take a litte while..."
    
    for link in link_list:
        print "Scraping {}".format(link)
        page = requests.get(link)
        file_loc = os.path.join(dir_, link.strip(url))
        #ensure_dirs(file_loc)

        #with codecs.open(file_loc + '`.html', 'w', 'utf-8') as f:
        with codecs.open(link + '.html', 'w', 'utf-8') as f:
            f.write(page.text)

        # dirty, hacky, horrible, please never do this
        try:
            print "Trying to get page JSON"
            link_json = link + '.json'
            page_json = json.loads(requests.get(link_json).text)
            #file_loc_json = os.path.join(dir_, link_json.strip(url))
            #ensure_dirs(file_loc_json)

            #with codecs.open(file_loc_json + '.html', 'w', 'utf-8') as f:
            with codecs.open(link_json, 'w', 'utf-8') as f:
                f.write(json.dumps(page_json))
            print "Success"
        except Exception:
            print "Failed"
            continue

def ensure_dirs(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


if __name__ == '__main__':
    scrape_recursively("http://www.restorethefourth.net/") 
