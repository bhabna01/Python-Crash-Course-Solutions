def make_album(name,album_name,songs=None):
    if songs:
        album={"Artist Name":name,"Album Name":album_name,"Number of songs":songs}
        return album
    else:
        album={"Artist Name":name,"Album Name":album_name}
        return album
print("Justin bieber","Believe",23)
print("Justin bieber","Believe")