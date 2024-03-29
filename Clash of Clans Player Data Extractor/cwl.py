import requests
api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjQ4MjAxNjM1LTUyYjgtNDc2Yy05MmQ2LWRlMjAyMzZlZjYyOSIsImlhdCI6MTcxMTcyNzI1Miwic3ViIjoiZGV2ZWxvcGVyL2JhNGM5MmJmLTU3ODYtMmM3My03YzdmLTJlOWViZDQ0MWE4YSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEyMi4xNjEuMjQyLjI5Il0sInR5cGUiOiJjbGllbnQifV19.K8oOQ3hjUMzuOVU7kdnuPxPmWlOwGq7du-YOblkBxwl7ZIQdDPEcCd3IszIWOBhLMKr97kR-Xke-dRxXndW4gQ'
headers = {
        'Authorization': f'Bearer {api_token}',
        }
clanTag = '%239CVRL9QQ'
url = f'https://api.clashofclans.com/v1/clans/%239cvrl9qq/warlog?limit=10'
response = requests.get(url, headers=headers)
warlog = response.json()
print(warlog)

import re
import datetime

def camel_to_title_case(key):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', key).title()


def caseChange(input_dict):
    result_dict = {}
    for key, value in input_dict.items():
        title_case_key = camel_to_title_case(key)
        result_dict[title_case_key] = value
    return result_dict


x = {'items': 
     [{
         'result': 'lose', 
         'endTime': '20240329T113644.000Z', 
         'teamSize': 40, 
         'attacksPerMember': 2, 
         'clan': {'tag': '#9CVRL9QQ', 
                  'name': 'BIG勉', 
                  'clanLevel': 24, 
                  'attacks': 51, 
                  'stars': 86, 
                  'destructionPercentage': 84.15, 
                  'expEarned': 484}, 
        'opponent': {
            'tag': '#YY8LQ8VC', 
            'name': '"Green Lantern"',  
            'clanLevel': 21, 
            'stars': 115, 
            'destructionPercentage': 96.3}}
            ]}


q = 0
for i in range(len(x['items'])):
    for j, k in x['items'][i].items():
        nj = camel_to_title_case(j)
        if j == 'endTime':
            y = datetime.datetime.strptime(k, '%Y%m%dT%H%M%S.%fZ')
            print(nj,y)
            continue
        if j == 'clan':
            print('Clan Stats')
            for v,s in x['items'][i][j].items():
                vv = camel_to_title_case(v)
                print(vv,s)
            continue
        if j == 'opponent':
            print('Opponent Stats')
            for vv,ss in x['items'][i][j].items():
                vvv = camel_to_title_case(vv)
                print(vvv,ss)
            continue
        print(nj,k)


f = {'items': 
     [{
         'result': 'lose', 
         'endTime': '20240329T113644.000Z', 
         'teamSize': 40, 
         'attacksPerMember': 2, 
         'clan': {
             'tag': '#9CVRL9QQ', 
             'name': 'BIG勉', 
             'badgeUrls': {'small': 'https://api-assets.clashofclans.com/badges/70/TqQjOJuOPIpkqZFHglRwhM3MYI9yGfVji9dmAey3X90.png', 'large': 'https://api-assets.clashofclans.com/badges/512/TqQjOJuOPIpkqZFHglRwhM3MYI9yGfVji9dmAey3X90.png', 'medium': 'https://api-assets.clashofclans.com/badges/200/TqQjOJuOPIpkqZFHglRwhM3MYI9yGfVji9dmAey3X90.png'}, 'clanLevel': 24, 'attacks': 51, 'stars': 86, 'destructionPercentage': 84.15, 'expEarned': 484}, 'opponent': {'tag': '#YY8LQ8VC', 'name': '"Green Lantern"', 'badgeUrls': {'small': 'https://api-assets.clashofclans.com/badges/70/lU7jvlXBvWLOGLRm3MQNd9WFLstQsZ04jOYWp-54qCA.png', 'large': 'https://api-assets.clashofclans.com/badges/512/lU7jvlXBvWLOGLRm3MQNd9WFLstQsZ04jOYWp-54qCA.png', 'medium': 'https://api-assets.clashofclans.com/badges/200/lU7jvlXBvWLOGLRm3MQNd9WFLstQsZ04jOYWp-54qCA.png'}, 'clanLevel': 21, 'stars': 115, 'destructionPercentage': 96.3}}, {'result': 'win', 'endTime': '20240327T105419.000Z', 'teamSize': 40, 'attacksPerMember': 2, 'clan': {'tag': '#9CVRL9QQ', 'name': 'BIG
勉', 'badgeUrls': {'small': 'https://api-assets.clashofclans.com/badges/70/TqQjOJuOPIpkqZFHglRwhM3MYI9yGfVji9dmAey3X90.png', 'large': 'https://api-assets.clashofclans.com/badges/512/TqQjOJuOPIpkqZFHglRwhM3MYI9yGfVji9dmAey3X90.png', 'medium': 'https://api-assets.clashofclans.com/badges/200/TqQjOJuOPIpkqZFHglRwhM3MYI9yGfVji9dmAey3X90.png'}, 'clanLevel': 24, 'attacks': 46, 'stars': 104, 'destructionPercentage': 88.95, 'expEarned': 508}, 'opponent': {'tag': '#2GC9GYYP', 'name': '파랑새', 'badgeUrls': {'small': 'https://api-assets.clashofclans.com/badges/70/y_ERiMcS2ItLmktuCma2-Ummic2owESGaKMir3hS7ZQ.png', 'large': 'https://api-assets.clashofclans.com/badges/512/y_ERiMcS2ItLmktuCma2-Ummic2owESGaKMir3hS7ZQ.png', 'medium': 'https://api-assets.clashofclans.com/badges/200/y_ERiMcS2ItLmktuCma2-Ummic2owESGaKMir3hS7ZQ.png'}, 'clanLevel': 15, 'stars': 34, 'destructionPercentage': 31.525}}, {'result': 'lose', 'endTime': '20240325T093318.000Z', 'teamSize': 40, 'attacksPerMember': 2, 'clan': {'tag': '#9CVRL9QQ', 'name': 'BIG勉', 'badgeUrls': {'small': 'https://api-assets.clashofclans.com/badges/70/TqQjOJuOPIpkqZFHglRwhM3MYI9yGfVji9dmAey3X90.png', 'large': 'https://api-assets.clashofclans.com/badges/512/TqQjOJu