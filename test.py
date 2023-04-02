import requests
import json

print("Hello world this works ")
url = 'https://api.cricapi.com/v1/currentMatches?apikey=8990f916-8107-4f70-9e8e-dcbd9639b687&offset=0'

download  = requests.get(url).text
json_data = json.loads(download)

print(json_data['data'])