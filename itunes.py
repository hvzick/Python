import sys
import requests
import json


artistName = input("Enter Artist name to search for his songs: ")
songLimit = input("Enter how many songs you want to search: ")

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit= {songLimit} &term= {artistName}")

if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()
    
no = 1 
for result in data["results"]:
    print(f"{no}) {result['trackName']}")
    no += 1
print("\n")