import requests
import json

headers = { 'Content-Type': 'application/json'}

def get_team_stats():
        #fetches all the the team from the best team

        api_url = 'https://statsapi.web.nhl.com/api/v1/teams?expand=team.stats'
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
                return json.loads(response.content.decode('utf-8'))
        else:
                return None

team_info = get_team_stats()

if team_info is not None:
    print("Successfully created the .JSON file")
    for team in team_info.items():
        with open('all_team_info.json', 'w') as f:
                print(json.dumps(team, indent=2), file=f)

else:
        print('[!] Request Failed')