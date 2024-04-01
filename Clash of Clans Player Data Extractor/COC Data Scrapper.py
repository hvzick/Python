import requests
import re
import os
import sys
import datetime
from Authorization import email
from Authorization import password
# Replace 'YOUR_API_TOKEN' with the actual API token you obtained
api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjQ4MjAxNjM1LTUyYjgtNDc2Yy05MmQ2LWRlMjAyMzZlZjYyOSIsImlhdCI6MTcxMTcyNzI1Miwic3ViIjoiZGV2ZWxvcGVyL2JhNGM5MmJmLTU3ODYtMmM3My03YzdmLTJlOWViZDQ0MWE4YSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEyMi4xNjEuMjQyLjI5Il0sInR5cGUiOiJjbGllbnQifV19.K8oOQ3hjUMzuOVU7kdnuPxPmWlOwGq7du-YOblkBxwl7ZIQdDPEcCd3IszIWOBhLMKr97kR-Xke-dRxXndW4gQ'

# Set up headers with the API token for authentication
headers = {
        'Authorization': f'Bearer {api_token}',
        }


def main():
    for file in os.listdir():
        if file.endswith('.txt'):
            os.unlink(file)
    while True:
        x = input('Enter Email: ').strip()
        y = input('Enter password: ').strip()
        if x == email() and y == password():
            print('\nAuthorization Successful\n')
            break
        else:
            print('Email or Password incorrect')

    while True:
        c = int(input('\nEnter 1 for player data\nEnter 2 for clan data\nEnter 0 to exit: \n'))
        if c == 1:
            playerdata()
        elif c == 2:
            clanData()
        elif c == 0:
             break


def clanData():
    clanTag = input('Enter clan tag: ').upper().strip()
    while True:
        x = int(input('\nEnter 1 for Clan Information\nEnter 2 for Clan Members Information\nEnter 2 for Current War Status\nEnter 4 for Clan Capital Details\nEnter 0 to return: '))
        match x:
            case 1:
                clanInfo(clanTag)
            case 2:
                clanMembers(clanTag)
            case 3:
                currentWar(clanTag)
            case 4:
                warlog(clanTag)
            case 0:
                return

def clanInfo(clanTag):
    url = f'https://api.clashofclans.com/v1/clans/%23{clanTag}'
    response = requests.get(url, headers=headers)
    data = response.json()
    x = caseChange(data)
    with open('1 Clan Information Data.txt', 'w', encoding='utf-8') as file:
        file.write(f"{' ' * 30} Clan Information Data\n")
        q = 1
        for i,j in x.items():
            if q == 9:
                break
            else:
                if i == 'Location':
                    for v,k in x['Location'].items():
                        newv = camel_to_title_case(v)
                        if 'Country' in v:
                            file.write(f'{newv}: {k}\n')
                        else:
                            file.write(f'Country {newv}: {k}\n')
                    continue
                elif i == 'Badge Urls':
                    continue
                elif i == 'Type':
                    jj = camel_to_title_case(j)
                    file.write(f'{i}: {jj}\n')
                    continue
                file.write(f'{i}: {j}\n')
            q += 1
    return 0
def warlog(clanTag):
    no = int(input('Enter number of wars: '))
    url = f'https://api.clashofclans.com/v1/clans/%23{clanTag}/warlog?limit={no}'  # Correctly format clanTag and no in the URL
    response = requests.get(url, headers=headers)
    x = response.json()
    with open('4 Clan Warlog.txt', 'w', encoding='utf-8') as file:
        file.write(f"{' ' * 30} Clan Warlog\n")
        t = -1
        for i in range(len(x['items'])):
            file.write(f"\n{' ' * 10}--->War Number {t}<---\n")
            for j, k in x['items'][i].items():
                nj = camel_to_title_case(j)
                if j == 'endTime':
                    y = datetime.datetime.strptime(k, '%Y%m%dT%H%M%S.%fZ')
                    file.write(f'{nj}: {y}\n')
                    continue
                if j == 'clan':
                    file.write(f"{' ' * 15} Clan Stats\n")
                    for v,s in x['items'][i][j].items():
                        if v == 'badgeUrls':
                            continue
                        vv = camel_to_title_case(v)
                        file.write(f'{vv}: {s}\n')
                    continue
                if j == 'opponent':
                    file.write(f"{' ' * 15} Opponent Stats\n")
                    for vv,ss in x['items'][i][j].items():
                        if vv == 'badgeUrls':
                            continue
                        vvv = camel_to_title_case(vv)
                        file.write(f'{vvv}: {ss}\n')
                    continue
                file.write(f'{nj}: {k}\n')
            t = t-1
    return 0




def currentWar(clanTag):
    url = f'https://api.clashofclans.com/v1/clans/%23{clanTag}/currentwar'

    response = requests.get(url, headers=headers)
    currentWar = response.json()
    with open('3 Current War Data.txt', 'w', encoding='utf-8') as file:
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

# 9cvrl9qq


def clanMembers(clanTag):
    url = f'https://api.clashofclans.com/v1/clans/%23{clanTag}/members'
    response = requests.get(url, headers=headers)
    clanMembers = response.json()
    with open('2 Clan Members Data.txt', 'w', encoding='utf-8') as file:
        i = 0

        file.write(f"{' ' * 30} Clan Members\n")
        for item in clanMembers['items']:
            for key, value in clanMembers['items'][i].items():
                if key in ['league', 'builderBaseLeague', 'playerHouse']:
                    continue
                title_case_key = camel_to_title_case(key)
                title_case_value = str(value).title()
                if title_case_key == 'Tag':
                    file.write(f'{i+1}.  {title_case_key}: {title_case_value}\n')

                    continue
                file.write(f'   {title_case_key}: {title_case_value}\n')
            file.write('\n')
            i += 1
    return 0



def playerdata():
    playerTag = input("Enter player tag: ").upper().strip()

    # Form the API endpoint URL
    url = f"https://api.clashofclans.com/v1/players/%23{playerTag}"

    # Make the API request  
    response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
    if response.status_code == 200:
        while True:
            x = int(input("\nEnter 1 for Player Data\nEnter 2 for Troop Data \nEnter 3 for Hero Data \nEnter 4 for Hero Equipment Data \nEnter 5 for Spell Data \nEnter 6 for Achievement Data\nEnter 0 to return: "))
            player_data = response.json()
            if x > 6 or x < 0:
                print(f"\nInvalid input: {x}\n")
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
                case 6:
                    achievementData(player_data)
                case 0:
                    return
    elif response.status_code == 404:
        sys.exit(f'Not player found with tag {playerTag}')
    # elif response.status_code == 403:
    #     sys.exit('Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.')
    # elif response.status_code == 503:
    #     sys.exit('Service is temprorarily unavailable because of maintenance.')
    # elif response.status_code == 429:
    #     sys.exit('Request was throttled, because amount of requests was above the threshold defined for the used API token.')
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
    with open('1 Player Data.txt', 'w') as file:
        file.write(f"{' ' * 30} Player Data\n")
        i = 0
        for key in newPlayerData:
            if i == 16:
                break
            else:
                file.write(f"{key}: {newPlayerData[key]}\n")
            i += 1
        file.write('\n')
    return 0


def troopData(player_data):
    with open('2 Troop Data.txt', 'w') as file:
        no = 1
        file.write(f"{' ' * 30} Troop Data\n")
        for n in player_data['troops']:
            file.write(f"{no}. {n['name']}: Level = {n['level']}/{n['maxLevel']}\n")
            no += 1
        file.write('\n')
    return 0


def heroData(player_data):
    with open('3 Hero Data.txt', 'w') as file:
        no = 1
        file.write(f"{' ' * 30} Hero Data\n")
        for n in player_data['heroes']:
            file.write(f"{no}. {n['name']}: Hero Level = {n['level']}/{n['maxLevel']}\n")
            no += 1
        file.write('\n')
    return 0


def heroEqpData(player_data):
    with open('4 Hero Equipment Data.txt', 'w') as file:
        no = 1
        file.write(f"{' ' * 30} Hero Equipment Data\n")
        for n in player_data['heroEquipment']:
            file.write(f"{no}. {n['name']}: Level = {n['level']}/{n['maxLevel']}\n")
            no += 1
        file.write('\n')
    return 0


def spellData(player_data):
    with open('5 Spell Data.txt', 'w') as file:
        no = 1
        file.write(f"{' ' * 30} Spell Data\n")
        for n in player_data['spells']:
            file.write(f"{no}. {n['name']}: Level = {n['level']}/{n['maxLevel']}\n")
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
    with open('6 Achievement Data.txt', 'w') as file:
        file.write(f"{' ' * 30} Achievements Data\n")
        no = 1
        for n in player_data['achievements']:
            file.write(f"{no}. Achievement Name: {n['name']}\n     Max:{n['stars']}\n     Current: {n['value']}\n     Target: {n['target']}\n     Information: {n['info']}\n     {n['completionInfo']}")
            file.write('\n')
            no += 1
            file.write('\n')
    return 0





if __name__ == "__main__":
    main()