from collector.core.http.request import Request
from collector.core.collector import Collector


class UnsplashCollector(Collector):
    name = 'unsplash'

    def start_requests(self):
        urls = [
            'https://unsplash.com/napi/topics/wallpapers/photos?page=1&per_page=50',
            'https://unsplash.com/napi/topics/wallpapers/photos?page=2&per_page=50'
        ]
        for url in urls:
            yield Request(url=url)

    def parse(self, response):
        pass
