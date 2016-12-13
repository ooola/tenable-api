Tenable API
===========

This repository contains sample commands for interacting with the Tenable (Nessus) api documented on <https://cloud.tenable.com/api#/overview>.

## Prerequisites

Set your user credentials in creds.json
```
{
  "username":"you@email.com",
  "password":""
}
```

## Common Commands

### Login to get a session token

First login to get a session cookie then include it as `X-Cookie` for subsequent requests.

```
#!/usr/bin/env python2.7

import requests
import json

with open('creds.json') as df:
  data = json.load(df)

session = requests.post('https://cloud.tenable.com/session', data = data)

headers = { 'X-Cookie': 'token=' + session.json()['token']}

requests.get('https://cloud.tenable.com/scanners', headers=headers)
. . .
```

### List available scanners

`list-scanners.py`

### Start scan of EC2 instance

`start-ec2-pci-scan.py` starts a pre-configured PCI scan of an internal (VPC) EC2 instance using a pre-configured Tenable (Nessus) scanner in the VPC.

### Print status

`print-scan-status.py` prints the status of existing scans. Scan with a status of 'complete' can be downloaded.

### Scan details

`scan-details.py` prints the details including the number of vulnerabilities from recent scans.

```
$ scan-details.py 15
. . .
 u'hosts': [{u'critical': 0,
             . . .
             u'hostname': u'ec2-35-164-212-193.us-west-2.compute.amazonaws.com',
             u'info': 14,
             u'low': 2,
             u'medium': 1,
             . . . 
             u'severitycount': {u'item': [{u'count': 14,
                                           u'severitylevel': 0},
                                          {u'count': 2,
                                           u'severitylevel': 1},
                                          {u'count': 1,
                                           u'severitylevel': 2},
                                          {u'count': 0,
                                           u'severitylevel': 3},
                                          {u'count': 0,
                                           u'severitylevel': 4}]},
```

15 is the scan id available from `print-scan-status.py`. This provide a means to report on new vulnerabilities.
