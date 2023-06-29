import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])

o = response.json()

# print the entire "response"
# print(o)

# print only the names of the songs
for result in o["results"]:
    print(result["trackName"])


