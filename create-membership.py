import requests
access_token = 'MjE2ZDMxNmEtMjMyOC00MTk5LWJjZTQtMWM1ZDQ4ODg1NzdmZjdmZTA0MTMtZjll_P0A1_4a252141-f787-4173-a4c9-bde69c553a24'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNWI1ZWI3YTAtZmFjOC0xMWVjLWI3MWYtYmY3OWFiZWFhYjc4'
person_email = '9isnaisna9@gmail.com'
url = 'https://webexapis.com/v1/memberships'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
 }
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())