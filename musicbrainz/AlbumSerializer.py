from .get_by_id import get_album_by_id

class AlbumSerializer():
    def general_info(self,id):
        insatnce=get_album_by_id(id)
        return insatnce