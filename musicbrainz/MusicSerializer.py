from .get_by_id import get_recording_by_id

class MusicSerializer():
    def general_info(self,id):
        insatnce=get_recording_by_id(id)
        return insatnce