import requests
import re
# Replace 'YOUR_API_TOKEN' with the actual API token you obtained
api_token1 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjQ4ZDQ0NzhhLWZhOWItNDZmMS1hMzQ1LTY2N2ExODY2ZDQ2NCIsImlhdCI6MTcwNTE1NjgxNSwic3ViIjoiZGV2ZWxvcGVyL2JhNGM5MmJmLTU3ODYtMmM3My03YzdmLTJlOWViZDQ0MWE4YSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE2OS4xNDkuMTk2LjI0MSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.1qrTewpjD_eRF7Ojb71OGR8HcsvUiHOUSWS7GKrLZxekPB7FO-_4dn7-oq6mI0JmVdVkVjNmyMAzlAdt-uIlHQ'
api_token2 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImI1YjJjZTY1LWEyNmEtNDZjZC1iZmMxLTk1YTZjODQ0Y2Q3MCIsImlhdCI6MTcwNTIxNjMyNywic3ViIjoiZGV2ZWxvcGVyL2JhNGM5MmJmLTU3ODYtMmM3My03YzdmLTJlOWViZDQ0MWE4YSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjIwNS4yNTMuMTAuMjExIl0sInR5cGUiOiJjbGllbnQifV19.9vlaxsDcmhVz7PUaSGhD7KicGRVzbd6pdq6fVlznmPbbYK7fldph4rIwGZfbE-12TQ7T5pUL8DXJIQFzN6xUBw'
api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjdjZTU1NTI2LWMzOGYtNGMwYi04ZDZjLWY0MjE4ZTY1YzM2NSIsImlhdCI6MTcwNTMwMzc4OSwic3ViIjoiZGV2ZWxvcGVyL2JhNGM5MmJmLTU3ODYtMmM3My03YzdmLTJlOWViZDQ0MWE4YSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEyMi4xNjEuMjQxLjE3NiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.oO2RkSFj_tENBkbeNqrg2t3cT4cib2NOGB6e5aqDWytOTcyy1pLhOsEF3FmvKnltewOU7VF9jftFRgIfFdBb1Q'
def main():
# Ask for player id
    playerTag = input("Enter player tag: ").upper().strip()

# Form the API endpoint URL
    url = f"https://api.clashofclans.com/v1/players/%23{playerTag}"

# Set up headers with the API token for authentication
    headers = {
    'Authorization': f'Bearer {api_token}',
    }
# Make the API request  
    response = requests.get(url, headers=headers)
    data(response)

def data(response):

# Check if the request was successful (status code 200)
    if response.status_code == 200:
        while True:
            x = int(input("\nEnter 1 for Troop Data\nEnter 2 for Troop Data \nEnter 3 for Hero Data \nEnter 4 for Hero Equipment Data \nEnter 5 for Spell Data \nEnter 0 to exit: "))
            player_data = response.json()
            if x > 4 or x < 0:
                print(f"Invalid input: {x}")
            match x:
                case 1:
                    playerData(player_data)
                case 2:
                    troopData(player_data)
                case 3:
                    heroData(player_data)
                case 4:
                    heroEqpData(player_data)
                case 5:
                    spellData(player_data)
                case 0:
                    break
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

def playerData(player_data):
    x = 0
    pd = {}
    for key in player_data:
        pd[key] = player_data[key]
        #print(f"{key}: {player_data[key]}")
        x += 1
        if x == 17:
            break
    newPlayerData = caseChange(pd)
    for key in newPlayerData:
        print(f"{key}: {newPlayerData[key]}")
    return

def troopData(player_data):
    no = 1
    for n in player_data['troops']:
        print(f"{no}) Troop Name = {n['name']}: Troop Level = {n['level']}/{n['maxLevel']}")
        no += 1
    return 0


def heroData(player_data):
    no = 1
    for n in player_data['heroes']:
        print(f"{no}) {n['name']}: Hero Level = {n['level']}/{n['maxLevel']}")
        no += 1
    return 0


def heroEqpData(player_data):
    no = 1
    for n in player_data['heroEquipment']:
        print(f"{no}) {n['name']}: Hero Level = {n['level']}/{n['maxLevel']}")
        no += 1
    return 0


def spellData(player_data):
    no = 1
    for n in player_data['spells']:
        print(f"{no}) {n['name']}: Hero Level = {n['level']}/{n['maxLevel']}")
        no += 1
    return 0

def camel_to_title_case(key):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', key).title()

def caseChange(input_dict):
    result_dict = {}
    for key, value in input_dict.items():
        title_case_key = camel_to_title_case(key)
        result_dict[title_case_key] = value
    return result_dict

def achievementData(player_data):
    no = 1
    for n in player_data['achievements']:
        print(f"{no}) {n['name']}:{n['stars']} {n['value']} {n['target']} {n['info']} {n['completionInfo']}")
        no += 1
    return 0





if __name__ == "__main__":
    main()