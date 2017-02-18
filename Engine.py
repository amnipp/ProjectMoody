import MoodFinder
from spotifyArtist import spotifyEngine as se
def get_valence():
    mf = MoodFinder.MoodFinder()
    mf.setResolution(640,480);
    avg = float(mf.calculateAverageValence())
    print("On a scale of 0 to 1, your mood is at about a " + str(avg))
    return avg

if __name__=='__main__':
    print('Welcome to mood playlists!')
    username = input("Please enter your name: ")
    print("Thank you,",str(username).capitalize())
    print("Let's see how you're feeling!")
    valence = get_valence()
    print(valence)
    spotify = se()
    name = spotify.get_user_top_artists()
    print("Your search will be based on the artist:" ,name,"\n")
    artist = spotify.get_artist(name)
    tracks = spotify.show_recommendations_by_valence(artist, valence)
    trackID = []

    for track in tracks:
        print(track['name'],", by ", track['artist'])