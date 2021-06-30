import spotipy
import requests
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

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

# Test 1 : Make sure response returns 200
# Test 2 : Make sure I get the album name and release_date
response = requests.get(BASE_URL + 'artists/' + drake_uri + '/albums', headers=headers,)
json_response = response.json()

names = []
release_dates = []
# Test 1 : Make sure the first 10 albums and release_dates are shown
for i in range(0,10):
  names.append(json_response['items'][i]['name'])
  release_dates.append(json_response['items'][i]['release_date'])
data = {
  'Album Name' : names,
  'Release_Date' : release_dates     
}
col_names = ['Album Name', 'Release_Date']
df = pd.DataFrame(data = data)

engine = create_engine('mysql://root:codio@localhost/album_info')
df.to_sql('albums', con=engine, if_exists='replace', index=False)