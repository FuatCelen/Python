
import sqlite3

def fetch_artists():
    connection =sqlite3.connect('chinook.db')
    cursor = connection.cursor()
    cursor.execute("SELECT artistid,Name FROM artists")
    artists = {row[0]: row[1] for row in cursor.fetchall()}
    connection.close()
    return artists

def fetch_albums_by_artists(artist_id):
    connection = sqlite3.connect('chinook.db')
    cursor = connection.cursor()
    cursor.execute ("SELECT Title FROM albums WHERE ArtistId = ?",(artist_id,))
    albums = cursor.fetchall()
    connection.close()
    return albums

def save_albums_to_html(artist_id, albums):
    html_content = "<html><body><table><tr><th>Album Title</th></tr>"
    for album in albums:
        html_content += "<tr><td>{}</td></tr>".format(album[0])
    html_content += "</table><body></html>"

    with open (f"a{artist_id}.html","w") as file:
        file.write(html_content)


def main():
    artists = fetch_artists()

    while True:
        artist_name = input("Enter the name of an artist (or type 'exit' to quit):")
        if artist_name.lower()=='exit':
            break

        artist_id = None

        for id, name in artists.items():
            if name.lower()== artist_name.lower():
                artist_id = id
                break

        if artist_id is not None:
            albums = fetch_albums_by_artists(artist_id)
            save_albums_to_html(artist_id,albums)
            print(f"Albums by {artist_name} have been saved to {artist_id}.html")

        else:
            print("Artist not found.")

main()