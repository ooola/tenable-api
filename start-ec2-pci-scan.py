#!/usr/bin/env python2.7

import requests
import json
import sys
from pprint import pprint

with open('creds.json') as df:
  data = json.load(df)

session = requests.post('https://cloud.tenable.com/session', data = data)

headers = { 'X-Cookie': 'token=' + session.json()['token']}

##
## Load configured scans
##
scans = requests.get('https://cloud.tenable.com/scans', headers=headers)

##
## Start a scan of our preconfigured EC2 instance
##
target = ''
for s in scans.json()['scans']:
  if s['name'] == 'Scan of EC2 instance':
    print 'found target id: %d' % s['id']
    target = s['id']
    break

if target == '':
  print 'unable to find target'
  sys.exit(1)

# launch new scan; note that an alternate target could be passed in
status = requests.post('https://cloud.tenable.com/scans/' + str(target) + '/launch', headers=headers)

pprint(status.json())
