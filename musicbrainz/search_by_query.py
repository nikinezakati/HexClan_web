import musicbrainzngs
import sys
from User.models import total_album_rating, total_artist_followings, total_music_rating
from musicbrainz.get_by_id import get_artist_by_id


musicbrainzngs.set_useragent(
    "HexClan",
    "0.1",
    "hex_clan",
)


def search_artist_by_name(query, limit, offset,photo):
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
                re['followings'] = query.following_num
            else:
                re['followings'] = None
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

        if 'life-span' in q:
            if 'begin' in q['life-span']:
                re['life-span'] = q['life-span']
            else:
                l = {}
                l['begin'] = '-'
                l['ended'] = q['life-span']['ended']
                re['life-span'] = l
        else:
            re['life-span'] = "-"
        if 'country' in q:
            re['country'] = q['country']
        else:
            continue
        
        if(photo):
            re_p=get_artist_by_id(q['id'])
            re['photo']=re_p['photo']

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

        # recording
        if 'id' in q:
            re['id'] = q['id']
            query = total_music_rating.objects.filter(music_id=q['id'])
            if len(query) != 0:
                if query.vote_num != 0:
                    re['rating'] = query.rating/query.vote_num
                else:
                    re['rating'] = None
            else:
                re['rating'] = None
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
                    if query.vote_num != 0:
                        re['rating'] = query.rating/query.vote_num
                    else:
                        re['rating'] = None
                else:
                    re['rating'] = None

                if photo:
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

            if 'first-release-date' in q:
                if q['first-release-date'] != " ":
                    re['first-release-date'] = q['first-release-date']
                else:
                    re['first-release-date'] = "-"
            else:
                re['first-release-date'] = "-"

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

# if __name__ == '__main__':
#     # recording='63e4c621-56a2-4d3f-99d9-25af98d0bede'
#     print(search_artist_by_name('Billie Eilish',0,0))
#     #print(get_album_by_id('a672261f-aa4a-43bd-9d83-2c031b1b77a4'))
#     #print(musicbrainzngs.get_image_list('61e374b6-1b37-481a-9c81-139317f1e59a'))

