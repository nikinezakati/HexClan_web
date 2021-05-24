import requests
from bs4 import BeautifulSoup
from .models import genre
import wikipedia
def get_genres_mb():
    r = requests.get('https://musicbrainz.org/genres')
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    uls = soup.find(id='content')
    for ul in uls:
        for li in ul.findAll('li'):
            if li.find('ul'):
                    break
            x = li.a.text.strip()
            y = GenresDescriptionsAPIView(x)
            genre.objects.create(name=li.a.text.strip(),genre_id=li.a['href'].strip().replace('/genre/', ''), description=y)
            print(x)
            print(y)



def GenresDescriptionsAPIView(str1):
	s = str1
	try:
		result = wikipedia.summary(s +' music', sentences=1)
		return result
	except:
		result = ""
		return result



