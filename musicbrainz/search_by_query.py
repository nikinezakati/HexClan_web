import musicbrainzngs
import sys
# from Page.models import *

musicbrainzngs.set_useragent(
    "HexClan",
    "0.1",
    "hex_clan",
)


def search_artist_by_name(query):
    annotations = musicbrainzngs.search_artists(query)
    qu = annotations['artist-list']
    artists = {}
    artists[0] = []
    for q in qu:
        re = {}
        if 'id' in q:
            re['id'] = q['id']
        else:
            break
        if 'name' in q:
            re['name'] = q['name']
        else:
            break
        if 'type' in q:
            re['type'] = q['type']
        else:
            break
        if 'ext:score' in q:
            if int(q['ext:score']) < 6:
                re['score'] = q['ext:score']
            else:
                re['score'] = str(int(q['ext:score'])/20)
        else:
            break
        if 'life-span' in q:
            re['life-span'] = q['life-span']
        else:
            break
        if not len(re)==0:
            artists[0].append(re)

    return artists


def search_recording_by_name(query):
    annotations = musicbrainzngs.search_recordings(query)
    qu = annotations['recording-list']
    recordings = {}
    recordings[0] = []
    for q in qu:
        re = {}
        re['artist'] = []
        re['album'] = []

        # recording
        if 'id' in q:
            re['id'] = q['id']
        else:
            break
        if 'title' in q:
            re['title'] = q['title']
        else:
            break
        if 'ext:score' in q:
            if int(q['ext:score']) < 6:
                re['score'] = q['ext:score']
            else:
                re['score'] = str(int(q['ext:score'])/20)
        else:
            break
        # artist
        if 'artist-credit' in q:
            for artist in q['artist-credit']:
                temp = {}
                if 'artist' in artist:
                    if 'id' in artist['artist']:
                        temp['id'] = artist['artist']['id']
                    else:
                        break
                    if 'name' in artist['artist']:
                        temp['name'] = artist['artist']['name']
                    else:
                        break
                    re['artist'].append(temp)
                else:
                    break
        else:
            break

        # album
        if 'release-list' in q:
            for release in q['release-list']:
                if 'date' in release:
                    re['date'] = release['date']
                else:
                    break
                if 'release-group' in release:
                    temp2 = {}
                    if 'type' in release['release-group'] and release['release-group']['type'] == 'Album':
                        if 'id' in release['release-group']:
                            temp2['id'] = release['release-group']['id']
                            # cover = musicbrainzngs.get_release_group_image_list(
                            #     release['release-group']['id'])
                            # if 'images' in cover and 'image' in cover['images'][0]:     
                            #     temp2['cover_image'] = cover['images'][0]['image']
                            # else:
                            #     break   
                        else:
                            break      
                        if 'title' in release['release-group']:
                            temp2['title'] = release['release-group']['title']
                        else:
                            break
                        re['album'].append(temp2)
                    else:
                        break
                else:
                    break
        else:
            break
        if not len(re)==0:    
            recordings[0].append(re)

    return recordings


def search_album_by_name(query):
    annotations = musicbrainzngs.search_release_groups(query)
    qu = annotations['release-group-list']
    albums = {}
    albums[0] = []

    for q in qu:
        re = {}
        re['artist'] = []

        if 'type' in q and q['type'] == 'Album':
            if 'id' in q:
                re['id'] = q['id']
            
                cover = musicbrainzngs.get_release_group_image_list(q['id'])
                if 'images' in cover and 'image' in cover['images'][0]:
                    re['cover_image'] = cover['images'][0]['image']
                else:
                    break 
            else:
                break     
            if 'title' in q:
                re['title'] = q['title']
            else:
                break
            if 'ext:score' in q:
                if int(q['ext:score']) < 6:
                    re['score'] = q['ext:score']
                else:
                    re['score'] = str(int(q['ext:score'])/20)
            else:
                break
            if 'first-release-date' in q:
                re['first-release-date'] = q['first-release-date']
            else:
                break

            # artist
            if 'artist-credit' in q:
                for artist in q['artist-credit']:
                    temp = {}
                    if 'artist' in artist:
                        if 'id' in artist['artist']:
                            temp['id'] = artist['artist']['id']
                        else:
                            break
                        if 'name' in artist['artist']:
                            temp['name'] = artist['artist']['name']
                        else:
                            break
                        re['artist'].append(temp)
                    else:
                        break
            else:
                break
        if not len(re['artist'])==0:    
            albums[0].append(re)

    return albums


