from collector.core.collector import Collector


class UnsplashCollector(Collector):
    name = 'unsplash'

    def start_requests(self):
        print('Yes, I did it!')
        pass

    def parse(self, response):
        pass
