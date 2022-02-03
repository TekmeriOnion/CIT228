from tkinter import N


print("-----------Exercise 8-7----------------")
def make_album(artist,title,songCount=None):
    """Create dictionaries that store key metadata about music albums"""
    album = {'artist':artist, 'title':title}
    if songCount:
        album['tracks'] = songCount
    return album

fiveLeaves = make_album('Nick Drake', 'Five Leaves Left')
print(fiveLeaves)

outbound = make_album('Bela Fleck & The Flecktones', 'Outbound')
print(outbound)

letItBe = make_album('The Beatles', 'Let It Be', 12)
print(letItBe)

print("-----------Exercise 8-8----------------")
print("Let's document your record collection, one album at a time")
userAlbums = {}
album_id = 1
quitter = False
while quitter != True:
    userAlbum = make_album(input("Enter artist: "), input("Enter album title: "))
    print(userAlbum)
    userAlbums[album_id] = userAlbum
    album_id += 1
    print("\n")
    quitCheck = input("Do you want to enter another album? Enter 'q' to quit; press any other key to continue: ")
    if quitCheck.lower() != 'q':
        continue
    else:
        print("Here's your completed record collection:")
        for album in userAlbums.items():
            print(album)
        break