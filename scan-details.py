#!/usr/bin/env python2.7

import requests
import json
import sys
from pprint import pprint

scanid = sys.argv[1]
if len(scanid) == 0:
  print 'please pass in scan id'
  sys.exit(1)

with open('creds.json') as df:
  data = json.load(df)

session = requests.post('https://cloud.tenable.com/session', data = data)

headers = { 'X-Cookie': 'token=' + session.json()['token']}

##
## Load configured scans
##
scans = requests.get('https://cloud.tenable.com/scans/' + scanid, headers=headers)

pprint(scans.json())
