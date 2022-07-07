import requests
import json
access_token = 'MjE2ZDMxNmEtMjMyOC00MTk5LWJjZTQtMWM1ZDQ4ODg1NzdmZjdmZTA0MTMtZjll_P0A1_4a252141-f787-4173-a4c9-bde69c553a24'
url = 'https://webexapis.com/v1/people/me'
headers = {
 'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
