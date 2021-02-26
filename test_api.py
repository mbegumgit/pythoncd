import requests
import datetime
from urllib import request
import json
# diferent way of accessing web server using API in json format

url = 'http://api.open-notify.org/astros.json'
url_json =request.urlopen(url)
data = json.load(url_json)
print(data)
print('end of printinng..')

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    # for item in obj['people']:
    #     print(item)
    # requests.get() function returns a response object; use the response.status_code attribute
    # to receive the status code for our request

# url = 'http://api.open-notify.org/this-api-doesnt-exist'
response = requests.get(url)
print(response.status_code)
jprint(response.json())
parameters = {
    "lat": 40.71,
    "lon": -74
}
response1 = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
pass_times = response1.json()['response']
jprint(pass_times)
risetimes = []
#Each pass time is a dictionary with risetime (pass start time) and duration keys
for d in pass_times:
    time = d['risetime']
    risetimes.append(time)
print(risetimes)
#use the Python datetime.fromtimestamp() method to convert these into easier to understand times
times = []

for rt in risetimes:
    time = datetime.date.fromtimestamp(rt)
    times.append(time)
    print(time)



