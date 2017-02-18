import MoodFinder
from spotifyArtist import spotifyEngine as se
def get_valence():
    print("Finding your current mood, please look at the camera for a few seconds...")
    mf = MoodFinder.MoodFinder()
    mf.setResolution(640,480);
    avg = float(mf.calculateAverageValence())
    print("On a scale of 0 to 1, your mood is at about a " + str(avg))
    return avg

if __name__=='__main__':
    valence = 0.33#get_valence()
    print(valence)
    spotify = se()
    name = spotify.get_user_top_artists()
    print("Your search will be based on the artist:" ,name)
    artist = spotify.get_artist(name)
    tracks = spotify.show_recommendations_by_valence(artist, valence)
    trackID = []
    for track in tracks:
        #print(track)
        trackID.append(track['id'])
    print(trackID)
    spotify.add_to_playlist(trackID)

