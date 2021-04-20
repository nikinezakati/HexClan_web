from __future__ import print_function
from __future__ import unicode_literals
import musicbrainzngs
import sys
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


def search_artist_by_name(query):
    annotations = musicbrainzngs.search_artists(query)
    qu = annotations['artist-list']
    artists = {}
    artists[query]=[]
    for q in qu:
        re = {}
        if 'id' in q:
            re['id'] = q['id']
        if 'name' in q:
            re['name'] = q['name']
        if 'type' in q:
            re['type'] = q['type']
        if 'ext:score' in q:
            re['score'] = q['ext:score']
        if 'life-span' in q:
            re['life-span'] = q['life-span']
        artists[query].append(re)

    return artists

def search_recording_by_name(query):
    annotations = musicbrainzngs.search_recordings(query)
    qu = annotations['recording-list']
    recordings = {}
    recordings[query]=[]
    for q in qu:
        re = {}
        re['artist']=[]
        re['album']=[]

        #recording
        if 'id' in q:
            re['id'] = q['id']
        if 'title' in q:
            re['title'] = q['title']
        if 'ext:score' in q:
            re['score'] = q['ext:score']

        #artist
        if 'artist-credit' in q:
            for artist in  q['artist-credit']:
                temp={}
                if 'artist' in artist:
                    if 'id' in artist['artist']:
                        temp['id'] = artist['artist']['id']
                    if 'name' in artist['artist']:
                        temp['name'] = artist['artist']['name']
                    re['artist'].append(temp)   

        #album
        if 'release-list' in q:
            for release in q['release-list']:
                if 'date' in release:         
                    re['date'] = release['date']  
                if 'release-group' in release:
                    temp2={}
                    if 'type' in release['release-group'] and release['release-group']['type']=='Album':         
                        if 'id' in release['release-group']:
                            temp2['id']=release['release-group']['id']
                        if 'title' in release['release-group']:
                            temp2['title']=release['release-group']['title']
                        re['album'].append(temp2)

        recordings[query].append(re)

    return recordings

def search_album_by_name(query):
    annotations = musicbrainzngs.search_release_groups(query)
    qu = annotations['release-group-list']
    albums = {}
    albums[query]=[]

    for q in qu:
        re = {}
        re['artist']=[]

        if 'type' in q and q['type']=='Album':
            if 'id' in q:
                re['id'] = q['id']
            if 'name' in q:
                re['name'] = q['name']
            if 'ext:score' in q:
                re['score'] = q['ext:score']
            if 'first-release-date' in q:
                re['first-release-date'] = q['first-release-date']

            #artist
            if 'artist-credit' in q:
                for artist in  q['artist-credit']:
                    temp={}
                    if 'artist' in artist:
                        if 'id' in artist['artist']:
                            temp['id'] = artist['artist']['id']
                        if 'name' in artist['artist']:
                            temp['name'] = artist['artist']['name']
                        re['artist'].append(temp)   
        albums[query].append(re)

    return albums    


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
#     print(search_album_by_name("x&Y"))
