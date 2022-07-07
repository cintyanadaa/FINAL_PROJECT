import requests
access_token = 'MjE2ZDMxNmEtMjMyOC00MTk5LWJjZTQtMWM1ZDQ4ODg1NzdmZjdmZTA0MTMtZjll_P0A1_4a252141-f787-4173-a4c9-bde69c553a24'
url = 'https://webexapis.com/v1/rooms'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params={'title': 'DevNet Associate Training!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
