#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """

import urllib

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
   html = response.read()
   print('Body response:')
   print('\t- type: {}'.format(type(html)))
   print('\t- content: {}'.format(html))
   print('\t- utf8 content: {}'.format(html.decode('utf-8')))
