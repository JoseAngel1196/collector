from typing import Iterable, List
from collector.core.models.user import User
from collector.core.models.photo import Photo
from collector.core.models.image import Image
from collector.core.http.request import Request
from collector.core.collector import Collector


class UnsplashCollector(Collector):
    name = "unsplash"

    def start_requests(self):
        urls = [
            "https://unsplash.com/napi/topics/wallpapers/photos?page=1&per_page=50",
        ]
        for url in urls:
            self.logger.info(f"Yielding request {url}")
            yield Request(url=url)

    def parse(self, response) -> Iterable[Photo]:
        photos = response.json()
        for photo in photos:
            photo_id = photo["id"]
            user = photo["user"]
            profile_image = user["profile_image"]
            yield Photo(
                photo_id=photo_id,
                title=photo["alt_description"],
                description=photo["alt_description"],
                photo_image=Image(
                    raw=photo["urls"]["raw"],
                    large=photo["urls"]["full"],
                    regular=photo["urls"].get("regular"),
                    small=photo["urls"]["small"],
                ),
                likes=photo["likes"],
                user=User(
                    user_id=user["id"],
                    username=user["username"],
                    first_name=user["first_name"],
                    last_name=user["last_name"],
                    portfolio_url=user["portfolio_url"],
                    bio=user["bio"],
                    profile_image=Image(
                        large=profile_image["large"],
                        regular=profile_image.get("regular"),
                        small=profile_image["small"],
                    ),
                ),
                instagram_username=user["instagram_username"],
                total_likes=user["total_likes"],
                total_photos=user["total_photos"],
                for_hite=user["for_hire"],
            )
