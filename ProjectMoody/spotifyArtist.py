import sys
import random
import spotipy
import json
import spotipy.util as util
import spotipy.oauth2 as oauth2

''' shows recommendations for the given artist
'''
class spotifyEngine():

    def __init__(self):
        with open('APIKEY.json') as dataFile:
            clientData = json.load(dataFile)
        user = 'possessedferret'
        scope = 'playlist-read-private playlist-read-collaborative user-follow-read user-library-read user-top-read'
        token = util.prompt_for_user_token(user, scope, redirect_uri="http://127.0.0.1:8888/callback/")
        self.sp = spotipy.Spotify(auth=token)
        spURL = '1228892812'
        self.sp.trace=False
        self.user = self.sp.user(spURL)

    def get_artist(self, name):
        artistsname = ""
        artistsname = artistsname + name
        results = self.sp.search(q=('artist:' + artistsname), type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            return items[0]
        else:
            return None

    def show_recommendations_for_artist(self,artist):
        albums = []
        results = self.sp.recommendations(seed_artists = [artist['id']])
        print(results['tracks'])
        for track in results['tracks']:
            print(track['name'], '-', track['artists'][0]['name'])

    def get_user_top_artists(self):
        artistsList = self.sp.current_user_top_artists(limit=20)
        r = random.randint(0,19)
        return artistsList['items'][r]['name']
    def add_to_playlist(self, tracks):
        user = self.sp.user('possessedferret')
        playlist = self.sp.user_playlist_create(user,'Mood Playlist')
        print(playlist)
        self.sp.user_playlist_add_tracks(user=user,playlist_id='Mood Playlist',tracks=tracks)
        return None

    def show_recommendations_by_valence(self, artist, valence):
        albums = []
        results = self.sp.recommendations(seed_artists=[artist['id']],target_valence=valence)
        audioList = []
        dict = []
        mood = 0
        for track in results['tracks']:
            audioList = self.sp.audio_features(track['id'])
            mood = audioList[0]['valence']
            energy = audioList[0]['energy']
            dict.append({'name':track['name'],
                         'id':track['id'],
                        'artist':track['artists'][0]['name'],
                        'valence': mood, 'energy':energy})
        return dict
"""
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(('Usage: {0} artist name'.format(sys.argv[0])))
    else:
        name = ' '.join(sys.argv[1:])
        artist = get_artist(name)
        if artist:
            show_recommendations_for_artist(artist)
        else:
            print("Can't find that artist", name)

    name = get_artist('Mac Miller')
    show_recommendations_by_valence(name)
"""