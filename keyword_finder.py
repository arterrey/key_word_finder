#!/usr/bin/env python

from urllib2 import urlopen
from lxml import etree
from StringIO import StringIO
import os.path
import sys
from hashlib import md5

cache_dir = "/tmp/keyword_cache"
def get_page(url):

    try:
        os.mkdir(cache_dir)
    except OSError:
        pass
        
    cache_name = cache_dir + "/" + md5(url).hexdigest()

    if os.path.isfile(cache_name):
        return open(cache_name, "r")
    else:
        response = urlopen(url)
        fout = open(cache_name, "w")
        fout.write(response.read())
        fout.close()
        fin = open(cache_name)
        return fin
        
        

def main():
    # Download a page
    argv = sys.argv
    page_url = argv[1]
    #page_url = "http://www.familyfocusdental.com.au"

    page = get_page(page_url)
    parser = etree.HTMLParser()
    tree = etree.parse(page, parser)
    
    import pdb; pdb.set_trace()

    # Look for keywords
    keywords = []
    
    # Print Keywords
    print keywords

if __name__ == "__main__":
    main()

