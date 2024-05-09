desde sql, hacer filtros de informacion, como jugadores elo>x cuantas veces gane o perdi

canciones_data = [] #Lista vacia para almacenar datos

albumes = sp.artist_albums(artista_id, album_type='album')
singles = sp.artist_albums(artista_id, album_type='single')

for album in albumes['items'] + singles['items']:
    album_nombre = ['album':'álbum', 'single':'canción'][album['album_type']]
    album_año = album['release_data'].split('-')[0]

	tracks = sp.album_tracks(album['id'])

