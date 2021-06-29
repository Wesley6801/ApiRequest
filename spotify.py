import spotipy
import requests

client_id = 'bb7e8950c9834eaea96062eb752e5ddf'
client_secret = '4a37f3ed348644959f6f1594fb24e915'
auth_url = "https://accounts.spotify.com/api/token"
auth_response = requests.post(auth_url,{
    'grant_type' : 'client_credentials',
    'client_id' : client_id,
    'client_secret' : client_secret,
})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
headers = {
  'Authorization' : 'Bearer {token}'.format(token=access_token)
}
BASE_URL = 'https://api.spotify.com/v1/'
drake_uri = '3TVXtAsR1Inumwj472S9r4'
r = requests.get(BASE_URL + 'artists/' + drake_uri + '/albums', headers=headers,)
r2 = r.json()
for key, value in r2.items():
    print(key, " : ", value)