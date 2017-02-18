import spotipy
import spotipy.util as util
import json


with open('APIKEY.json') as dataFile:
    clientData = json.load(dataFile)
#os.environ['SPOTIPY_CLIENT_ID'] = clientData['clientID']
#os.environ['SPOTIPY_CLIENT_SECRET'] = clientData['clientSecret']
#os.environ['SPOTIPY_REDIRECT_URI'] = 'http://127.0.0.1:8888/callback/'

user = 'possessedferret'
scope='playlist-read-private playlist-read-collaborative user-follow-read user-library-read user-top-read'
token = util.prompt_for_user_token(user, scope, redirect_uri="http://127.0.0.1:8888/callback/")
sp = spotipy.Spotify(auth=token)
print(sp.user_playlists(user))
def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

def show_recommendations_for_artist(artist):
    albums = []
    results = sp.recommendations(seed_artists = [artist['id']])
    print(results['tracks'])
    for track in results['tracks']:
        print(track['name'], '-', track['artists'][0]['name'])

show_recommendations_for_artist(get_artist('Flight of the Conchords'))

"""
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
playlistTracks = get_playlist_tracks(user)
followingTracks = get_following_tracks(user)
songInfo = []
for track in playlistTracks['items']:
    songInfo.append(sp.audio_features(tracks=track['track']['id']))
print(songInfo)
print(len(songInfo))

def get_playlist_tracks(spUser):
    username = spUser
    playlists = sp.user_playlists(user=user, limit=50)

    for playlist in playlists['items']:
        trackList = sp.user_playlist_tracks(user=playlist['owner']['id'], playlist_id=playlist['uri'])
    print(trackList)
    return trackList
def get_following_tracks(spUser):
    username = spUser
    playlists = sp.user

"""
