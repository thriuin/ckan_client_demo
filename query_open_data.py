__author__ = 'Statistics Canada'
__copyright__ = 'Crown Copyright, Canada 2014'

import urllib2
import json

# Provide the fields to match. E.g. looking for a record with the specific ID e418841e-d9dc-4caf-9a19-09b3269a3e1e
query_data = urllib2.quote(json.dumps({'id': '9b25e61a-89c3-4719-afd8-fc61c7aeba0c'}))

# query the site using the CKAN web API
try:
    response = urllib2.urlopen('http://data.gc.ca/data/api/action/package_show', query_data)
except urllib2.HTTPError, hx:
    print hx.__str__()
    exit()

if response.code == 200:
    response_data = json.loads(response.read())

    if response_data['success'] is True:
        print(json.dumps(response_data, indent=2))

