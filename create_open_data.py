__author__ = 'Statistics Canada'
__copyright__ = 'Crown Copyright, Canada 2014'

import urllib2
import simplejson as json

# Add a new data set. For this example, we will use the NAICS 2012 dataset from Statistics Canada

# Ensure the data set does not already exist. Exit if it does
query_data = urllib2.quote(json.dumps({'id': '9b25e61a-89c3-4719-afd8-fc61c7aeba0c'}))
found = False
try:
    # Use a valid URL
    response = urllib2.urlopen('http://data.gc.ca/test/api/3/action/package_show', query_data)
    if response.code == 200:
        print "Data set already exists."
        exit()
except urllib2.HTTPError, hx:

    # If the data set is not found, a 404 exception is thrown
    if hx.code == 404:
        "Data set not found. Proceeding..."
    else:
        print "Unexpected error: " + hx.__str__()
        exit()

# Load the JSON and call the CKAN API function package_create()

try:
    new_ds = json.load(open("new_data_set.json"))
except json.JSONDecodeError, jx:
    print('Invalid JSON: ' + jx.__str__())

# Encode the JSON for the HTTP header

new_ds_string = urllib2.quote(json.dumps(new_ds))

# Call the CKAN API function package_create(). Use a valid URL
request = urllib2.Request('http://data.gc.ca/test/api/action/package_create')

# Replace xxxx... with an appropriate API Key
request.add_header('Authorization', 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')

try:
    response = urllib2.urlopen(request, new_ds_string)
    print "CKAN Return Code: " + response.code
except urllib2.HTTPError, hx:
    print hx.__str__()
