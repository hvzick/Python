import requests
import re
import os
import sys
import datetime

# Replace 'YOUR_API_TOKEN' with the actual API token you obtained
api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjViMDMxMDRhLTRjMmEtNGI1Yy1iYjdkLWRjNTY4YmE5YzM3ZiIsImlhdCI6MTcwNjYzNDg1Niwic3ViIjoiZGV2ZWxvcGVyL2JhNGM5MmJmLTU3ODYtMmM3My03YzdmLTJlOWViZDQ0MWE4YSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEyMi4xNjEuMjQxLjkzIl0sInR5cGUiOiJjbGllbnQifV19.ChUuPQS8aMjgz4aYEYdtTvHGGPhTnJ1mz5-6cMBBjX2f9kTtOxb5CMt74c3eYyNYzGVZc28BE8xhbDu5u9NisA'

# Set up headers with the API token for authentication
headers = {
        'Authorization': f'Bearer {api_token}',
        }
def main():
    
    for file in os.listdir():
        if file.endswith('.txt'):
            os.unlink(file)
    c = int(input('Enter 1 for player data\nEnter 2 for clan data: '))
    if c == 1:
    # Ask for player id
        playerTag = input("Enter player tag: ").upper().strip()

    # Form the API endpoint URL
        url = f"https://api.clashofclans.com/v1/players/%23{playerTag}"

    # Make the API request  
        response = requests.get(url, headers=headers)
        playerdata(response, playerTag)
    elif c == 2:
        clanTag = input('Enter clan tag: ').upper().strip()
        clanData(clanTag)


def clanData(clanTag):
    while True:
        x = int(input('Enter 1 for Clan Members Information\nEnter 2 for Current War Status\nEnter 3 for Clan Warlog\nEnter 0 to exit: '))
        match x:
            case 1:
                clanMembers(clanTag)
            case 2:
                currentWar(clanTag)
            case 3:
                warlog(clanTag)
            case 0:
                return 
            


def warlog(clanTag):
    url = 'https://api.clashofclans.com/v1/clans/%23{clanTag}/warlog'
    response = requests.get(url, headers=headers)
    warlog = response.json()
    print(warlog)


def currentWar(clanTag):
    url = f'https://api.clashofclans.com/v1/clans/%23{clanTag}/currentwar'
    response = requests.get(url, headers=headers)
    currentWar = response.json()
    with open('Player Data.txt', 'a', encoding='utf-8') as file:
        file.write(f"{' ' * 30} Clan War Information\n")
        for key in currentWar:
            if key in ['clan', 'opponent']:
                break
            if key in ['endTime', 'startTime', 'preparationStartTime']:
                t = currentWar[key]
                currentWar[key] = datetime.datetime.strptime(t, '%Y%m%dT%H%M%S.%fZ')
            k = camel_to_title_case(key)
            v = str(currentWar[key]).title()
            file.write(f'Clan War {k}: {v}\n')
        file.write(f"\n{' ' * 30} My clan War Status\n")
        for key, value in currentWar['clan'].items():
            if key == 'badgeUrls':
                continue
            if key == 'members':
                break
            k = camel_to_title_case(key)
            file.write(f'{k}: {value}\n')
        file.write(f"\n{' ' * 30} My clan War Members\n")
        no = 1
        for i in range(len(currentWar['clan']['members'])):
            for key, value in  currentWar['clan']['members'][i].items():
                k = camel_to_title_case(key)
                if k == 'Tag':
                    file.write(f'{no}.  {k}: {value}\n')
                    no += 1
                    continue
                file.write(f'    {k}: {value}\n')
            file.write('\n')
        file.write(f"\n{' ' * 30} Enemy Clan War Status\n")
        for key, value in currentWar['opponent'].items():
            if key == 'badgeUrls':
                continue
            if key == 'members':
                break
            k = camel_to_title_case(key)
            file.write(f'{k}: {value}\n')
        file.write(f"\n{' ' * 30} Enemy clan War Members\n")
        no = 1
        for i in range(len(currentWar['clan']['members'])):
            for key, value in  currentWar['opponent']['members'][i].items():
                k = camel_to_title_case(key)
                if k == 'Tag':
                    file.write(f'{no}.  {k}: {value}\n')
                    no += 1
                    continue
                file.write(f'    {k}: {value}\n')
            file.write('\n')
    return 0
    

    return 0


# 20C2GRC0Q



def clanMembers(clanTag):
    url = f'https://api.clashofclans.com/v1/clans/%23{clanTag}/members'
    response = requests.get(url, headers=headers)
    clanMembers = response.json()
    with open('Player Data.txt', 'a', encoding='utf-8') as file:
        i = 0
        file.write(f"{' ' * 30} Clan Members\n")
        for item in clanMembers['items']:
            for key, value in clanMembers['items'][i].items():
                if key in ['league', 'builderBaseLeague', 'playerHouse']:
                    continue
                title_case_key = camel_to_title_case(key)
                title_case_value = str(value).title()
                file.write(f'{title_case_key}: {title_case_value}\n')
            file.write('\n')
            i += 1
    return 0

def playerdata(response, playerTag):

# Check if the request was successful (status code 200)
    if response.status_code == 200:
        while True:
            x = int(input("\nEnter 1 for Player Data\nEnter 2 for Troop Data \nEnter 3 for Hero Data \nEnter 4 for Hero Equipment Data \nEnter 5 for Spell Data \nEnter 0 to exit: "))
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
    elif response.status_code == 404:
        sys.exit(f'Not player found with tag {playerTag}')
    elif response.status_code == 403:
        sys.exit('Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.')
    elif response.status_code == 503:
        sys.exit('Service is temprorarily unavailable because of maintenance.')
    elif response.status_code == 429:
        sys.exit('Request was throttled, because amount of requests was above the threshold defined for the used API token.')
    else:
        print(f"Error: {response.status_code} {response.text}")

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
    with open('Player Data.txt', 'a') as file:
        file.write(f"{' ' * 30} Player Data\n")
        for key in newPlayerData:
            file.write(f"{key}: {newPlayerData[key]}\n")
        file.write('\n')
    return 0

def troopData(player_data):
    with open('Player Data.txt', 'a') as file:
        no = 1
        file.write(f"{' ' * 30} Troop Data\n")
        for n in player_data['troops']:
            file.write(f"{no}. Troop Name = {n['name']}: Troop Level = {n['level']}/{n['maxLevel']}\n")
            no += 1
        file.write('\n')
    return 0


def heroData(player_data):
    with open('Player Data.txt', 'a') as file:
        no = 1
        file.write(f"{' ' * 30} Hero Data\n")
        for n in player_data['heroes']:
            file.write(f"{no}. {n['name']}: Hero Level = {n['level']}/{n['maxLevel']}\n")
            no += 1
        file.write('\n')
    return 0


def heroEqpData(player_data):
    with open('Player Data.txt', 'a') as file:
        no = 1
        file.write(f"{' ' * 30} Hero Equipment Data\n")
        for n in player_data['heroEquipment']:
            file.write(f"{no}. {n['name']}: Hero Level = {n['level']}/{n['maxLevel']}\n")
            no += 1
        file.write('\n')
    return 0


def spellData(player_data):
    with open('Player Data.txt', 'a') as file:
        no = 1
        file.write(f"{' ' * 30} Spell Data\n")
        for n in player_data['spells']:
            file.write(f"{no}. {n['name']}: Hero Level = {n['level']}/{n['maxLevel']}\n")
            no += 1
        file.write('\n')
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
    with open('Player Data.txt', 'a') as file:
        file.write(f"{' ' * 30} Achievements Data\n")
        no = 1
        for n in player_data['achievements']:
            print(f"{no}. {n['name']}:{n['stars']} {n['value']} {n['target']} {n['info']} {n['completionInfo']}")
            no += 1
            file.write('\n')
    return 0





if __name__ == "__main__":
    main()