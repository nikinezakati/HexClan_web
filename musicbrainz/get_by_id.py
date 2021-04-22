import musicbrainzngs
import sys
from datetime import datetime
# from Page.models import *

musicbrainzngs.set_useragent(
    "HexClan",
    "0.1",
    "hex_clan",
)

# def get_tracklist(artist, album):
#     result = musicbrainzngs.search_releases(
#         artist=artist, release=album, limit=1)
#     id = result["release-list"][0]["id"]

#     new_result = musicbrainzngs.get_release_by_id(
#         id, includes=["recordings", "release-groups"])
#     t = (new_result["release"]["medium-list"][0]["track-list"])
#     #date = (new_result['release']['release-group']['first-release-date'])

#     for x in range(len(t)):
#         line = (t[x])
#         # print(line)

#         # print(f'{line["number"]}. {line["recording"]["id"]}')


def get_artist_by_id(id):
    annotations = musicbrainzngs.get_artist_by_id(id,includes=["ratings"])
    qu = annotations['artist']
    artist = {}

    if 'id' in qu:
        artist['id'] = qu['id']
    if 'name' in qu:
        artist['name'] = qu['name']
    if 'type' in qu:
        artist['type'] = qu['type']
    if 'rating' in qu:
        artist['rating'] = qu['rating']['rating']
    if 'life-span' in qu:
        artist['life-span'] = qu['life-span']

    return artist
    
# def get_recording_by_id(id):
#     annotations = musicbrainzngs.get_recording_by_id(id,includes=['artists','work-rels','release-group-rels'])
#     qu = annotations['recording']
#     recording = {}

#     if 'id' in qu:
#         recording['id'] = qu['id']
#     if 'title' in qu:
#         recording['title'] = qu['title']
#     if 'type' in qu:
#         recording['type'] = qu['type']
#     if 'rating' in qu:
#         recording['rating'] = qu['rating']['rating']
#     if 'life-span' in qu:
#         recording['life-span'] = qu['life-span']

#     return recording

# def search_events():
#     now = datetime.now()
#     date = now.strftime("%Y")

#     annotations = musicbrainzngs.browse_labels(date)
#     qu = annotations['recording']
#     recording = {}

#     if 'id' in qu:
#         recording['id'] = qu['id']
#     if 'title' in qu:
#         recording['title'] = qu['title']
#     if 'type' in qu:
#         recording['type'] = qu['type']
#     if 'rating' in qu:
#         recording['rating'] = qu['rating']['rating']
#     if 'life-span' in qu:
#         recording['life-span'] = qu['life-span']

#     return recording

# if __name__ == '__main__':
#     # get first release
#     # if len(sys.argv) > 1:
#     #     artist, album = [sys.argv[1], sys.argv[2]]
#     #     get_tracklist(artist, album)
#     # else:
#     #     artist = input("Artist: ")
#     #     album = input("Album: ")
#     #     if not artist == "" and not album == "":
#     #         get_tracklist(artist, album)
#     #     else:
#     #         print("Artist or Album missing")
#     print(search_events())