import sys
import json
import requests
API_URL = "https://www.censys.io/api/v1"
UID = "0"
SECRET = "0"
def get(page):
    data = {
        "query":"443.https.tls.certificate.parsed.subject.organizational_unit: FortiGate", 
        "page":int(page), 
        "fields":["ip"]
    }
    res = requests.post(API_URL + "/search/ipv4", data=json.dumps(data), auth=('932a9c5d-6bfc-4e68-974e-92fc8e14c471', 'ajCGARrdM81nGE2BU5ORr8V8JUZVLqF5')).text
    # print(res)
    results = json.loads(res)
    for result in results["results"]:
        print "%s" % (result["ip"])
for i in range(1,50):
    get(i)