#!/usr/bin/env python2.7

import requests
import json
from pprint import pprint

with open('creds.json') as df:
  data = json.load(df)

session = requests.post('https://cloud.tenable.com/session', data = data)

headers = { 'X-Cookie': 'token=' + session.json()['token']}

s = requests.get('https://cloud.tenable.com/scanners', headers=headers)

pprint(s.json())
