#!/usr/bin/python
# encoding: utf8
"""
cleader - CLI READER

Store web articles as plain text. No more 'saved as' HTML (aka cURL:d) or
'printed as PDF', just extracted content in markdown, without all annoying markup.

CLI:

    cleader.py [--save[=.]] <url>

Python:

    import cleader
    url = 'an url I want the body of'
    token = 'a Readability Parser API token'
    text = cleader.cleader(url, token)

"""

from __future__ import print_function
import datetime
import html2text
import json
import os
import re
import sys
import urllib
import urllib2

token = 'readability_api_parser_token_here' # retreived for free at readability.com

def cleader(url, token=token, save_dir=None):
    content = Readability(token).request(url)
    plaintext = basic_decorator(content)
    slugify = lambda value: "".join([x.lower() if x.isalnum() else "_" for x in value])
    if save_dir:
        filename = save_dir+os.sep+slugify(content['title'])+".md"
        if os.path.exists(filename):
            raise Exception("Cowardly refusing to overwrite "+filename)
        with open(filename, 'w') as f:
            f.write(plaintext.encode('utf-8'))
    else:
        print(plaintext)

class Readability():
    base_url = 'http://www.readability.com/api/content/v1/parser'
    def __init__(self, parser_api_token):
        self.token = parser_api_token
    def request(self, url):
        response = urllib2.urlopen(self.base_url+"?"+urllib.urlencode({
            'token': self.token,
            'url': url
        }))
        # @todo: handle errors.. not that they would ever occur
        return json.loads(response.read())

def basic_decorator(args):
    if 'content' not in args:
        raise Exception("No 'content' found in response")
    content = html2text.html2text(args['content'])
    if 'title' in args and args['title']:
        content = "# "+args['title']+"\n\n"+content
    if 'author' in args and args['author']:
        content += "\nBy: "+args['author']
    if 'date' in args and args['date']:
        content += "\n\Written at: "+args['date']
    content += "\nURL: "+args['url']
    content += "\nFetched at: "+datetime.datetime.now().strftime("%c")
    return content

def _fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)

def main():
    save_dir = None
    url = None
    for arg in sys.argv:
        if arg.startswith('--save='):
            save_dir = os.path.expanduser(arg[len('--save='):]).rstrip(os.sep)
        elif arg.startswith('--save'):
            save_dir = '.'
        elif arg == __file__:
            # otherwise we complain about 'unknown arg' a bit too often..
            continue
        elif not url:
            url = arg
        else:
            _fail("Unkown option: "+arg)

    if not url:
        _fail("Usage: cleader.py [--save[=.]] <url>")

    try:
        cleader(url, save_dir=save_dir)
    except Exception as e:
        _fail(e)

if __name__ == '__main__':
    main()
