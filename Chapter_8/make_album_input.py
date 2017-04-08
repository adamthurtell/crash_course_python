def make_album(album_title, artist_name, tracks=''):
    """Return a dictionary about an album"""
    album = {'artist': artist_name, 'album': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("\nEnter the album information")
    print("(enter 'q' at any time to quit)")

    analbum = input("Album name: ")
    if analbum == 'q':
        break

    artist = input("Artist name: ")
    if artist == 'q':
        break

    track_nmbr = input("How many tracks ('return' to leave blank): ")
    if track_nmbr == 'q':
        break

    album_info = make_album(analbum, artist, track_nmbr)
    print(album_info)