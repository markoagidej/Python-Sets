# Task 1: Artist Lineup Compilation

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()

for artist in artist_names:
    unique_artists.add(artist)

print(unique_artists)


# Task 2: Genre Sorting

artists_genres = {
    "The Lumineers": "Folk",
    "Tame Impala": "Psychedelic Rock",
    "Billie Eilish": "Pop",
    "Arctic Monkeys": "Indie Rock"
}

genre_artists = {}
for artist, genre in artists_genres.items():
    if genre not in genre_artists:
        genre_artists[genre] = {artist}
    else:
        genre_artists[genre].add(artist)

print(genre_artists)


# Task 3: Playlist Duplication Check

import copy

playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}

playlists = [playlist1, playlist2, playlist3]

for playlist in playlists:
    filtered_playlists = copy.deepcopy(playlists)
    filtered_playlists.remove(playlist)

    if playlist in filtered_playlists:
        print("Duplicate playlist found!")
        break
    
    print("No duplicated playlist found!")