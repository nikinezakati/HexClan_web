
from .get_by_id import get_artist_by_id

class ArtistSerializer():
    def general_info(self,id):
        insatnce=get_artist_by_id(id)
        return insatnce