__author__ = 'Statistics Canada'
__copyright__ = 'Crown Copyright, Canada 2014'

import urllib2
import simplejson as json

# Add or update a data set. For this example, we will use the NAICS 2012 dataset from Statistics Canada

# Step 1. Validate the existence of the data set.

query_data = urllib2.quote(json.dumps({'id': '9b25e61a-89c3-4719-afd8-fc61c7aeba0c'}))
found = False
try:
    # Use a valid URL
    response = urllib2.urlopen('http://data.gc.ca/test/api/3/action/package_show', query_data)
    if response.code == 200:
        found = True
except urllib2.HTTPError:
    print "Unable to locate data set"
    exit()

# Verify the response sent back by CKAN was successful

if found:
    response_data = json.loads(response.read())

    if response_data['success'] is True:

        # Load the example JSON record from a file

        try:
            dataset_revision = json.load(open("updated_data_set.json"))
            print(json.dumps(dataset_revision, indent=2 * ' '))
        except json.JSONDecodeError, jx:
            print('Invalid JSON: ' + jx.__str__())
            exit()

        # Call the CKAN API function package_update

        dataset_revision_enc = urllib2.quote(json.dumps(dataset_revision))

        # Use a valid URL
        request = urllib2.Request('http://data.gc.ca/test/api/action/package_update')

        # Replace xxxx... with an appropriate API Key
        request.add_header('Authorization', 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')

        try:
            response = urllib2.urlopen(request, dataset_revision_enc)
            print response
        except urllib2.HTTPError, hx:
            print hx.__str__()





