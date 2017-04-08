def make_album(artist_name, album_title, tracks=''):
    """Return a dictionary about an album"""
    album = {'artist': artist_name, 'album': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

analbum =make_album('white stripes', 'white blood cells')
print(analbum)

analbum = make_album('raconteurs', 'broken boy soldiers', '10')
print(analbum)
