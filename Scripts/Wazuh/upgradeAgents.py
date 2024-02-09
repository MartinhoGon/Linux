########################################
##   Developed By Martinho Gonçalves  ##
##             09/02/2024             ##
########################################

import requests
from getpass import getpass

requests.packages.urllib3.disable_warnings()

hostname="https://localhost:55000"

def loginApi(user, password):
    url=hostname+"/security/user/authenticate"
    print("Getting Token...")
    params = {
        'raw': 'true',
    }
    req = requests.get(
        url,
        params=params,
        verify=False,
        auth=(user, password)
    )
    try:
        response = req.json()
        if response["title"] == "Unauthorized":
            print(response["detail"])
            return 0
    except:
        token = req.text
        return token


def getAgentsToUpgrade(token):
    print("Getting agents that need to be upgraded...")
    headers = {
        'Authorization': 'Bearer ' + token,
    }
    params = {
        'pretty': 'true',
    }
    url=hostname+"/agents/outdated"
    req = requests.get(url, 
        params=params, 
        headers=headers,
        verify=False
    )
    agents = []
    response = req.json()
    for agent in response["data"]["affected_items"]:
        print(agent["id"])
        agents.append(agent["id"])
    return agents

def upgradeAgents(token, agentList):
    headers = {
        'Authorization': 'Bearer ' + token,
    }
    params = {
        'agents_list': agentList,
        'pretty': 'true',
    }
    url=hostname+"/agents/upgrade"
    req = requests.put(url,
        params=params,
        headers=headers,
        verify=False
    )
    print(req.json())

###################
# ---- MAIN ----- # 
###################

print("Upgrade wazuh agents")

apiUser = input('API user: ')
apiPass = getpass('Api Password: ')

token = loginApi(apiUser, apiPass)
if token == 0:
    exit()


agentsToUpgrade = getAgentsToUpgrade(token)
if len(agentsToUpgrade) == 0:
    print("There are no agents that need to be upgraded.")
    print("Exiting...")
    exit()

print('There are {} agents that need to be upgraded'.format(len(agentsToUpgrade)))

upgrade = input('Upgrade the agents? (y/n) ')

if upgrade == 'y' or upgrade == 'Y':
    agentList = ",".join(agentsToUpgrade);
    print(agentList)
    upgradeAgents(token, agentList)
else:
    print("Exiting...")
    exit()
