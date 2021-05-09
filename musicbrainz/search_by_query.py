import musicbrainzngs
import sys
# from Page.models import *

musicbrainzngs.set_useragent(
    "HexClan",
    "0.1",
    "hex_clan",
)


def search_artist_by_name(query, limit, offset):
    annotations = musicbrainzngs.search_artists(query, limit=limit, offset=offset)
    qu = annotations['artist-list']
    artists = {}
    artists['results'] = []
    for q in qu:
        re = {}
        if 'id' in q:
            re['id'] = q['id']
        else:
            continue
        if 'name' in q:
            re['name'] = q['name']
        else:
            continue
        if 'type' in q:
            re['type'] = q['type']
        else:
            continue
        if 'ext:score' in q:
            if int(q['ext:score']) < 6:
                re['score'] = q['ext:score']
            else:
                re['score'] = str(int(q['ext:score'])/20)
        else:
            continue
        if 'life-span' in q:
            re['life-span'] = q['life-span']
        else:
            continue
        if not len(re) == 0:
            artists['results'].append(re)

    return artists


def search_recording_by_name(query, limit, offset):
    date = "2005";
    annotations = musicbrainzngs.search_recordings(query,limit=limit,offset=offset,date=date,)
    qu = annotations['recording-list']
    recordings = {}
    recordings['results'] = []
    for q in qu:
        re = {}
        re['artist'] = []
        re['album'] = []

        # recording
        if 'id' in q:
            re['id'] = q['id']
        else:
            continue
        if 'title' in q:
            re['title'] = q['title']
        else:
            continue
        if 'ext:score' in q:
            if int(q['ext:score']) < 6:
                re['score'] = q['ext:score']
            else:
                re['score'] = str(int(q['ext:score'])/20)
        else:
            continue
        # artist
        if 'artist-credit' in q:
            for artist in q['artist-credit']:
                temp = {}
                if 'artist' in artist:
                    if 'id' in artist['artist']:
                        temp['id'] = artist['artist']['id']
                    else:
                        continue
                    if 'name' in artist['artist']:
                        temp['name'] = artist['artist']['name']
                    else:
                        continue
                    re['artist'].append(temp)
                else:
                    continue
        else:
            continue

        # album
        if 'release-list' in q:
            for release in q['release-list']:
                if 'date' in release:
                    re['date'] = release['date']
                else:
                    continue
                if 'release-group' in release:
                    temp2 = {}
                    if 'type' in release['release-group'] and release['release-group']['type'] == 'Album':
                        if 'id' in release['release-group']:
                            temp2['id'] = release['release-group']['id']
                            try:
                                cover = musicbrainzngs.get_release_group_image_list(
                                    release['release-group']['id'])
                                if 'images' in cover and 'image' in cover['images'][0]:
                                    temp2['cover_image'] = cover['images'][0]['image']
                                else:
                                    continue
                            except:
                                continue        
                        else:
                            continue
                        if 'title' in release['release-group']:
                            temp2['title'] = release['release-group']['title']
                        else:
                            continue
                        re['album'].append(temp2)
                    else:
                        continue
                else:
                    continue
        else:
            continue
        if not len(re) == 0:
            recordings['results'].append(re)

    return recordings


def search_album_by_name(query, limit, offset):
    annotations = musicbrainzngs.search_release_groups(query,limit=limit,offset=offset)
    qu = annotations['release-group-list']
    albums = {}
    albums['results'] = []

    for q in qu:
        re = {}
        re['artist'] = []

        if 'type' in q and q['type'] == 'Album':
            if 'id' in q:
                re['id'] = q['id']
                try:
                    cover = musicbrainzngs.get_release_group_image_list(
                        q['id'])
                    if 'images' in cover and 'image' in cover['images'][0]:
                        re['cover_image'] = cover['images'][0]['image']
                    else:
                        continue
                except:
                    continue
            else:
                continue
            if 'title' in q:
                re['title'] = q['title']
            else:
                continue
            if 'ext:score' in q:
                if int(q['ext:score']) < 6:
                    re['score'] = q['ext:score']
                else:
                    re['score'] = str(int(q['ext:score'])/20)
            else:
                continue
            if 'first-release-date' in q:
                re['first-release-date'] = q['first-release-date']
            else:
                continue

            # artist
            if 'artist-credit' in q:
                for artist in q['artist-credit']:
                    temp = {}
                    if 'artist' in artist:
                        if 'id' in artist['artist']:
                            temp['id'] = artist['artist']['id']
                        else:
                            continue
                        if 'name' in artist['artist']:
                            temp['name'] = artist['artist']['name']
                        else:
                            continue
                        re['artist'].append(temp)
                    else:
                        continue
            else:
                continue
        if not len(re['artist']) == 0:
            albums['results'].append(re)

    return albums


def top_artists(ID):
    annotations = musicbrainzngs.get_artist_by_id(id = ID)
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

def top_musics(ID):
    annotations = musicbrainzngs.get_recording_by_id(id = ID)
    return annotations

def top_albums(ID):
    annotations = musicbrainzngs.get_release_group_by_id(id = ID)
    return annotations
    
if __name__ == '__main__':
    # get first release
    # if len(sys.argv) > 1:
    #     artist, album = [sys.argv[1], sys.argv[2]]
    #     get_tracklist(artist, album)
    # else:
    #     artist = input("Artist: ")
    #     album = input("Album: ")
    #     if not artist == "" and not album == "":
    #         get_tracklist(artist, album)
    #     else:
    #         print("Artist or Album missing")
    print(search_artist_by_name('billie eilish'))