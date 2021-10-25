import requests
import yaml
import sys, os

file = open(os.path.join(sys.path[0], "api_key.yaml"))
secret = yaml.full_load(file)

# Google Place API only returns five results so we'll have to make multiple queries
places = []

# Paris
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=archéo%2018%20arrondissement&key=" + secret["key"]

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
places.append(response.text)
