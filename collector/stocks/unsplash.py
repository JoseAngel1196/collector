from collector.core.models.user import User
from collector.core.models.photo import Photo
from collector.core.models.image import Image
from collector.core.http.request import Request
from collector.core.collector import Collector


class UnsplashCollector(Collector):
    name = 'unsplash'

    def start_requests(self):
        urls = [
            'https://unsplash.com/napi/topics/wallpapers/photos?page=1&per_page=50',
        ]
        for url in urls:
            yield Request(url=url)

    def parse(self, response):
        photos = []
        for photo in response.json():
            photos.append(Photo(
                photo_id=photo['id'],
                title=photo['alt_description'],
                description=photo['alt_description'],
                urls=Image(
                    raw=photo['urls']['raw'],
                    full=photo['urls']['full'],
                    regular=photo['urls']['regular'],
                    small=photo['urls']['small'],
                ),
                likes=photo['likes'],
            ))
        return photos
