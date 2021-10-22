import requests

# Google Place API only returns five results so we'll have to make multiple queries
places = []

# Paris
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=archéo%2018%20arrondissement&key=AIzaSyC1hPxGQ258UePGhTHNvICRuUKb2cgP8hg"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
places.append(response.text)
