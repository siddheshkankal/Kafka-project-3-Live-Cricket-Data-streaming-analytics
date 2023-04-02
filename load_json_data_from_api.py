import requests
import csv
import os
import json


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'

# r = requests.get(url)
# data = r.json()

# print(data)

# --------------------------------------------

# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo&datatype=csv'


# download  = requests.get(url)
# decode_content = download.content.decode('utf-8')
# # rows = csv.reader(decode_content.splitlines(),delimiter=',')
# # data_list = list(rows)
# # for row in data_list:
# #     print(row)
# # print(decode_content)

# -------------------------------------------------------------

url = 'https://api.cricapi.com/v1/currentMatches?apikey=8990f916-8107-4f70-9e8e-dcbd9639b687&offset=0'

download  = requests.get(url).text
# decode_content = download.content.decode('utf-8')
# print((download))
json_data = json.loads(download)
# print(json_data['data'][0]['name'])
# print((json_data['data'][0]))
# print(list(json_data['data'][0].keys()))

for i in range(len(json_data['data'])):
    print(json_data['data'][i])
