import musicbrainzngs
import sys
from User.models import total_album_rating, total_artist_followings, total_music_rating
from musicbrainz.get_by_id import get_artist_by_id


musicbrainzngs.set_useragent(
    "HexClan",
    "0.1",
    "hex_clan",
)


def search_artist_by_name(query, limit, offset, photo):
    annotations = musicbrainzngs.search_artists(
        query, limit=limit, offset=offset)
    qu = annotations['artist-list']
    artists = {}
    artists['results'] = []
    for q in qu:
        re = {}
        if 'id' in q:
            re['id'] = q['id']
            query = total_artist_followings.objects.filter(artist_id=q['id'])
            if len(query) != 0:
                for l in query:
                    re['followings'] = l.following_num
            else:
                re['followings'] = 0
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

        l={}
        if 'life-span' in q:
            l['begin'] = '-'
            l['end'] ='-'
            l['span']='-'
            if 'begin' in q['life-span']:
                l['begin'] = q['life-span']['begin']
                if 'ended' in q['life-span']:
                    if q['life-span']['ended']=="false":
                        l['span']=f"{q['life-span']['begin'][0:4]}-present"
                    else:
                        if 'end' in q['life-span']:
                            l['end']=q['life-span']['end']
                            l['span']=f"{q['life-span']['begin'][0:4]}-{q['life-span']['end'][0:4]}"
            re['life_span']=l

        if 'country' in q:
            re['country'] = q['country']
        else:
            continue

        if(photo):
            re_p = get_artist_by_id(q['id'])
            re['photo'] = re_p['photo']

        if len(re) > 1:
            artists['results'].append(re)

    return artists


def search_recording_by_name(query, limit, offset, photo):
    annotations = musicbrainzngs.search_recordings(
        query, limit=limit, offset=offset)
    qu = annotations['recording-list']
    recordings = {}
    recordings['results'] = []
    for q in qu:
        re = {}
        re['artist'] = []
        re['album'] = []

        # rating
        if 'id' in q:
            re['id'] = q['id']
            query = total_music_rating.objects.filter(music_id=q['id'])
            if len(query) != 0:
                for l in query:
                    if l.vote_num != 0:
                        re['rating'] = l.rating
                    else:
                        re['rating'] = 0
            else:
                re['rating'] = 0
        else:
            continue
        if 'title' in q:
            re['title'] = q['title']
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
                if 'release-group' in release:
                    temp2 = {}
                    if 'type' in release['release-group'] and release['release-group']['type'] == 'Album':
                        if 'id' in release['release-group']:
                            temp2['id'] = release['release-group']['id']
                            if photo:
                                try:
                                    cover = musicbrainzngs.get_release_group_image_list(
                                        release['release-group']['id'])
                                    if 'images' in cover and 'image' in cover['images'][0]:
                                        temp2['cover_image'] = cover['images'][0]['image']
                                    else:
                                        temp2['cover_image'] = "http://127.0.0.1:8000/media/Images/defaultmusic.jpg" 
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
        if len(re['album']) == 0:
            temp2 = {}
            temp2['cover_image'] = "http://127.0.0.1:8000/media/Images/defaultmusic.jpg" 
            re['album'].append(temp2)

        if len(re) > 1:
            recordings['results'].append(re)

    return recordings


def search_album_by_name(query, limit, offset, photo):
    annotations = musicbrainzngs.search_release_groups(
        query, limit=limit, offset=offset)
    qu = annotations['release-group-list']
    albums = {}
    albums['results'] = []

    for q in qu:
        re = {}
        re['artist'] = []

        if 'type' in q and q['type'] == 'Album':
            if 'id' in q:
                re['id'] = q['id']
                query = total_album_rating.objects.filter(album_id=q['id'])
                if len(query) != 0:
                    for l in query:
                        if l.vote_num != 0:
                            re['rating'] = l.rating
                        else:
                            re['rating'] = 0
                else:
                    re['rating'] = 0

                if photo:
                    try:
                        cover = musicbrainzngs.get_release_group_image_list(
                            q['id'])
                        if 'images' in cover and 'image' in cover['images'][0]:
                            re['cover_image'] = cover['images'][0]['image']
                        else:
                            re['cover_image']  = "http://127.0.0.1:8000/media/Images/defaultalbum.jpg" 
                    except:
                        continue
            else:
                continue
            if 'title' in q:
                re['title'] = q['title']
            else:
                continue

            if 'first-release-date' in q:
                if q['first-release-date'] != " ":
                    re['first-release-date'] = q['first-release-date']
                else:
                    re['first-release-date'] = "_"
            else:
                re['first-release-date'] = "_"

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
        if len(re) > 1:
            albums['results'].append(re)
    return albums

