def make_album(name,album_name,songs=None):
    if songs:
        album={"Artist Name":name,"Album Name":album_name,"Number of songs":songs}
        return album
    else:
        album={"Artist Name":name,"Album Name":album_name}
        return album
while True:
    print("\n Please Enter the artist's name:")
    print("(Enter 'q' to quit any time)")
    artist_name=input("Artist Name: ")
    if  artist_name=='q':
        break

    album_name=input("Album Name: ")
    if album_name=='q':
        break
    songs=input("Number of songs")
    if songs==None:
        print(make_album(artist_name,album_name))
    else:
        print(make_album(artist_name,album_name,songs))
       
