import json
import requests

def get_playlist_images(CLIENT_ID, CLIENT_SECRET, playlist_id, mac_username):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    grant_type = 'client_credentials'
    body_params = {'grant_type' : grant_type}

    token_url='https://accounts.spotify.com/api/token'
    token_response = requests.post(token_url, data=body_params, auth=(CLIENT_ID, CLIENT_SECRET))

    token_raw = json.loads(token_response.text)
    token = token_raw["access_token"]
    header = {"Authorization": "Bearer {}".format(token)}
    playlist_response = requests.get(url, headers=header)
    playlist_raw = json.loads(playlist_response.text)

    for playlist_item in playlist_raw['items']:
        with open(f"/Users/{mac_username}/Downloads/{playlist_item['track']['album']['name']}.jpeg", 'wb') as file:
            file.write(requests.get(playlist_item['track']['album']['images'][0]['url']).content)
    print('Image retrieval complete, check your Downloads folder.')
        