import musicbrainzngs
from datetime import datetime
from User.models import total_album_rating, total_artist_followings, total_music_rating


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

def get_artistname_by_id(id):
    annotations = musicbrainzngs.get_artist_by_id(id, includes=['releases'])
    qu = annotations['artist']
    artist = {}
    artist['photo'] = ''

    if 'id' in qu:
        artist['id'] = qu['id']
    else:
        return {}    
    if 'name' in qu:
        artist['name'] = qu['name']   
    else:
        return {}   

    for release in qu['release-list']:
        temp = {}
        if len(artist['photo']) == 0:
            try:
                cover = musicbrainzngs.get_image_list(release['id'])
                if 'images' in cover and 'image' in cover['images'][0]:
                    artist['photo'] = cover['images'][0]['image']
            except:
                pass   
        if len(artist['photo']) != 0:
            break
    if len(artist['photo']) == 0:
        artist['photo'] = "http://127.0.0.1:8000/media/Images/defaultartist.jpg"  
    return artist    


def get_albumname_by_id(id):
    annotations = musicbrainzngs.get_release_group_by_id(id)

    qu = annotations['release-group']
    album = {}

    if 'primary-type' in qu and qu['primary-type'] == 'Album':
        if 'id' in qu:
            album['id'] = qu['id']
        else:
            return {}
        if 'title' in qu:
            album['title'] = qu['title']
        else:
            return {}

        try:
            cover = musicbrainzngs.get_release_group_image_list(id)
            if 'images' in cover and 'image' in cover['images'][0]:
                album['cover_image'] = cover['images'][0]['image']
            else:
                return {}
        except:
            album['cover_image'] = ''    
    if len(album['cover_image']) == 0:
        artist['photo'] = "http://127.0.0.1:8000/media/Images/defaultalbum.jpg"  
    return album     
    
def get_recordingname_by_id(id):
    annotations = musicbrainzngs.get_recording_by_id(id,includes=['releases'])
    qu = annotations['recording']

    recording = {}

    if 'id' in qu:
        recording['id'] = qu['id']
    else:
        return {}

    if 'title' in qu:
        recording['title'] = qu['title']
    else:
        return {}   

    if 'release-list' in qu:
        for release in qu['release-list']:
            temp = {}
            if len(recording['photo']) == 0:
                try:
                    cover = musicbrainzngs.get_image_list(release['id'])
                    if 'images' in cover and 'image' in cover['images'][0]:
                        recording['photo'] = cover['images'][0]['image']
                except:
                    pass   
            if len(recording['photo']) != 0:
                break            
        if len(recording['photo']) == 0:
            recording['photo'] = "http://127.0.0.1:8000/media/Images/defaultmusic.jpg"  
    return recording        



def get_artist_by_id(id):
    annotations = musicbrainzngs.get_artist_by_id(id, includes=['releases'])
    qu = annotations['artist']
    artist = {}
    artist['photo'] = ''

    if 'id' in qu:
        artist['id'] = qu['id']
    if 'name' in qu:
        artist['name'] = qu['name']
    if 'type' in qu:
        artist['type'] = qu['type']
    if 'country' in qu:
        artist['country'] = qu['country']    
    l={}
    if 'life-span' in qu:
        l['begin'] = '-'
        l['end'] ='-'
        l['span']='-'
        if 'begin' in qu['life-span']:
            l['begin'] = qu['life-span']['begin']
            if 'ended' in qu['life-span']:
                if qu['life-span']['ended']=="false":
                    l['span']=f"{qu['life-span']['begin'][0:4]}-present"
                else:
                    if 'end' in qu['life-span']:
                        l['end']=qu['life-span']['end']
                        l['span']=f"{qu['life-span']['begin'][0:4]}-{qu['life-span']['end'][0:4]}"
        artist['life_span']=l

    # releases
    for release in qu['release-list']:
        temp = {}
        if len(artist['photo']) == 0:
            try:
                cover = musicbrainzngs.get_image_list(release['id'])
                if 'images' in cover and 'image' in cover['images'][0]:
                    artist['photo'] = cover['images'][0]['image']
            except:
                pass   
        if len(artist['photo']) != 0:
            break
    if len(artist['photo']) == 0:
        artist['photo'] = "http://127.0.0.1:8000/media/Images/defaultartist.jpg"
    #followings
    query=total_artist_followings.objects.all().filter(artist_id=id)
    if len(query) !=0:
        for l in query:
            if l.artist_id==id:
                artist['followings']=l.following_num
    else:
        artist['followings']=None

    return artist

   


def get_album_by_id(id):
    annotations = musicbrainzngs.get_release_group_by_id(
        id, includes=['tags', 'artists', "releases", 'recording-rels'])

    qu = annotations['release-group']
    album = {}
    album['artist'] = []
    album['genre'] = []

    if 'primary-type' in qu and qu['primary-type'] == 'Album':
        if 'id' in qu:
            album['id'] = qu['id']
        else:
            return {}
        try:
            cover = musicbrainzngs.get_release_group_image_list(id)
            if 'images' in cover and 'image' in cover['images'][0]:
                album['cover_image'] = cover['images'][0]['image']
            else:
                return {}
        except:
            album['cover_image'] = "http://127.0.0.1:8000/media/Images/defaultalbum.jpg"
        if 'title' in qu:
            album['title'] = qu['title']
        else:
            return {}
        if 'first-release-date' in qu:
            album['release-date'] = qu['first-release-date']
        else:
            return {}

        # artist
        if 'artist-credit' in qu:
            for artist in qu['artist-credit']:
                temp = {}
                if 'id' in artist['artist']:
                    temp['id'] = artist['artist']['id']
                else:
                    return {}
                if 'name' in artist['artist']:
                    temp['name'] = artist['artist']['name']
                if 'type' in artist['artist']:
                    temp['type'] = artist['artist']['type']
                else:
                    return {}
                album['artist'].append(temp)
        else:
            return {}

        # genre
        if 'tag-list' in qu:
            for genre in qu['tag-list']:
                album['genre'].append(genre['name'])

        # rating
        query= total_album_rating.objects.all().filter(album_id=id)
        if len(query) !=0:
            for l in query:
                if l.vote_num !=0:
                    album['rating']=l.rating/l.vote_num
            else:
                album['rating']=None
        else:
            album['rating']=None

    else:
        return {}

    return album


def get_recording_by_id(id):
    annotations = musicbrainzngs.get_recording_by_id(
        id, includes=['artists', 'artist-rels', 'releases'])
    qu = annotations['recording']

    recording = {}
    recording['artist'] = []
    recording['album'] = []

    if 'id' in qu:
        recording['id'] = qu['id']
    else:
        return {}
    if 'title' in qu:
        recording['title'] = qu['title']
    else:
        return {}

    # rating
    query= total_music_rating.objects.all().filter(music_id=id)
    if len(query) !=0:
        for l in query:
            if l.vote_num !=0:
                recording['rating']=l.rating/l.vote_num
        else:
            recording['rating']=None
    else:
        recording['rating']=None

    # artist
    if 'artist-credit' in qu:
        for artist in qu['artist-credit']:
            temp = {}
            if 'artist' in artist:
                if 'id' in artist['artist']:
                    temp['id'] = artist['artist']['id']
                else:
                    return {}
                if 'type' in artist['artist']:
                    temp['type'] = artist['artist']['type']
                else:
                    return {}
                if 'name' in artist['artist']:
                    temp['name'] = artist['artist']['name']
                else:
                    return {}
                recording['artist'].append(temp)
    else:
        return {}

    # album
    if 'release-list' in qu:
        for album in qu['release-list']:
            temp = {}
            if 'id' in album:
                temp['id'] = album['id']
            else:
                return {}
            if 'title' in album:
                temp['title'] = album['title']
            else:
                return {}
            if 'date' in album:
                temp['date'] = album['date']
            else:
                return {}
            try:
                cover = musicbrainzngs.get_image_list(album['id'])
                if 'images' in cover and 'image' in cover['images'][0]:
                    temp['photo'] = cover['images'][0]['image']
            except:
                temp['photo'] = "http://127.0.0.1:8000/media/Images/defaultmusic.jpg"     
            recording['album'].append(temp)
    return recording

def browse_artist_music_by_id(id):
    annotations = musicbrainzngs.browse_recordings(id)
    result = {}
    result['result']=[]
    for qu in annotations['recording-list']:
        temp={}
        if 'id' in qu:
            temp['id']=qu['id']
        else:
            continue    
        if 'title' in qu:
            temp['title']=qu['title']
        else:
            continue
        if len(temp)>0 :
                result['result'].append(temp)
    return result['result']

def browse_artist_album_by_id(id):
    annotations = musicbrainzngs.browse_release_groups(id)
    result = {}
    result['result']=[]
    for qu in annotations['release-group-list']:
        temp={}
        if 'id' in qu:
            temp['id']=qu['id']
        else:
            continue    
        if 'type' in qu:
            temp['type']=qu['type']
        else:
            continue
        if 'title' in qu:
            temp['title']=qu['title']
        else:
            continue
        if 'first-release-date' in qu:
            temp['release_date']=qu['first-release-date']
        else:
            temp['release_date']='-'
        if len(temp)>0 :
                result['result'].append(temp)
   
    return result['result']


# if __name__ == '__main__':
#     # recording='63e4c621-56a2-4d3f-99d9-25af98d0bede'
#     print(get_artist_by_id('f4abc0b5-3f7a-4eff-8f78-ac078dbce533'))
#     #print(get_album_by_id('a672261f-aa4a-43bd-9d83-2c031b1b77a4'))
#     #print(musicbrainzngs.get_image_list('61e374b6-1b37-481a-9c81-139317f1e59a'))