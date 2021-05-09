import musicbrainzngs
from datetime import datetime
from User.models import music_rating,album_rating,artist_rating


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
    annotations = musicbrainzngs.get_artist_by_id(id)
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

    query=artist_rating.objects.filter(artist_id=id)
    temp=0
    for q in query:
        temp+=q.rating
        if len(query)!=0:
            artist['rating']=temp/len(query)
        else:
            artist['rating']=None

    return artist


def get_album_by_id(id):
    annotations = musicbrainzngs.get_release_group_by_id(
        id, includes=['tags','artists', "releases",'recording-rels'])
    
    qu = annotations['release-group']
    album={}
    album['artist'] = []
    album['genre'] = []

    if 'primary-type' in qu and qu['primary-type']=='Album':
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
            album['cover_image'] = ''
        if 'title' in qu:
            album['title'] = qu['title']
        else:
            return {}  
        if 'first-release-date' in qu:
            album['release-date'] = qu['first-release-date']
        else:
            return {}     

        #artist
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

        #genre
        if 'tag-list' in qu:
            for genre in qu['tag-list']:
                album['genre'].append(genre['name'])

        #rating
        query=album_rating.objects.filter(album_id=id)
        temp=0
        for q in query:
            temp+=q.rating
            if len(query) !=0:
                album['rating']=temp/len(query)
            else:
                album['rating']=None

    else:
        return {}   


    return album    
    
def get_recording_by_id(id):
    annotations = musicbrainzngs.get_recording_by_id(id,includes=['artists','artist-rels','releases'])
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

    #rating
        query=music_rating.objects.filter(music_id=id)
        temp=0
        for q in query:
            temp+=q.rating
            if len(query) != 0:
                recording['rating']=temp/len(query)
            else:
                recording['rating']=None
    #artist
    if 'artist-credit' in qu:
        for artist in qu['artist-credit']:
            temp = {}
            if 'artist' in artist:
                if 'id' in artist['artist']:
                    temp['id']=artist['artist']['id']
                else:
                    return {}    
                if 'type' in artist['artist']:
                    temp['type']=artist['artist']['type']
                else:
                    return {}    
                if 'name' in artist['artist']:
                    temp['name']=artist['artist']['name'] 
                else:
                    return {}
                recording['artist'].append(temp)    
    else:
        return {}   

    #album
    if 'release-list' in qu:
        for album in qu['release-list']:
            temp={}
            if 'id' in album:
                temp['id']=album['id'] 
            else:
                return {}        
            if 'title' in album:
                temp['title']=album['title'] 
            else:
                return {}        
            if 'date' in album:
                temp['date']=album['date'] 
            else:
                return {} 
            recording['album'].append(temp)            

    return recording



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
#     #recording='63e4c621-56a2-4d3f-99d9-25af98d0bede'
#     #print(get_artist_by_id('f4abc0b5-3f7a-4eff-8f78-ac078dbce533'))
#     #print(get_album_by_id('a672261f-aa4a-43bd-9d83-2c031b1b77a4'))
#     #print(musicbrainzngs.get_release_group_image_list('a672261f-aa4a-43bd-9d83-2c031b1b77a4'))
   