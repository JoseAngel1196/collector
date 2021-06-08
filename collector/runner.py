from logging import log
from typing import Iterable, List

from collector.core.models.photo import Photo
from collector.core.db_connector import DbConnector
from collector.logger import CollectorLogger
from collector.core.http.request import Request
from collector.core.http.downloader import Downloader
from collector.core.collector import Collector
from collector.core.stock_loader import StockLoader
from collector.settings import Settings
from collector.utils.project import get_project_settings
from collector.core.settings import DB_NAME, HOST, PASSWORD, PORT, USER

logger = CollectorLogger(__name__)


class CollectorRunner:

    stock_loader = StockLoader()

    def __init__(self, settings=None):
        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)
        self.settings = settings
        self.downloader = Downloader()
        self.db = DbConnector(
            dbname=DB_NAME,
            user=USER,
            pswd=PASSWORD,
            host=HOST,
            port=PORT,
            logger=logger,
        )

    def run(self):
        try:
            logger.info("Creating collector_cls")
            self.collectorcls = self.stock_loader.load(self.settings.stock_name)
            logger.info("Creating collector")
            self.collector = self._create_collector(self.collectorcls)
            logger.info("Starting a new requests")
            start_requests = self.collector.start_requests()
            logger.info("Opening the collector")
            self._open_collector(start_requests)
        except Exception as e:
            raise e

    def _create_collector(self, collectorcls) -> Collector:
        return collectorcls.from_runner(logger)

    def _open_collector(self, start_requests: List[Iterable[Request]]):
        print(start_requests)
        for start_request in start_requests:
            request_proceeded = self._process_request(start_request)

            logger.info(
                "Got request_proceeded", extra={"request_proceeded": request_proceeded}
            )

            request_parsed = self.collector.parse(request_proceeded)
            self._save_photo(request_parsed)
            logger.info("request saved")

    def _process_request(self, request: Iterable[Request]):
        method = getattr(self.downloader, request.method)
        return method(url=request.url)

    def _save_photo(self, photo: Iterable[Photo]):
        photo = next(photo)
        save_request_query = f"""
            WITH photo AS (
                INSERT INTO photos(
                    title,
                    description,
                    likes,
                    tags,
                    categories,
                    published_at,
                    stock_type
                ) VALUES ('{photo.title}', '{photo.description}', '{photo.likes}', {photo.tags}, {photo.categories}, {photo.published_at}, '{self.collector.name}')
                RETURNING photo_id
            )

            INSERT INTO photo_images(
                raw,
                small,
                regular,
                large,
                photo_id
            ) VALUES ('{photo.photo_image.raw}', '{photo.photo_image.small}', '{photo.photo_image.regular}', '{photo.photo_image.large}', new_photo_id);

            WITH users as (
                INSERT INTO users(
                username,
                first_name,
                last_name,
                portfolio_url,
                bio,
                full_name,
                instagram_username,
                twitter_username,
                total_likes,
                total_photos,
                for_hire,
                photo_id
            ) VALUES ('{photo.user.username}', '{photo.user.first_name}', '{photo.user.last_name}', '{photo.user.portfolio_url}', '{photo.user.bio}', '{photo.user.full_name}', '{photo.user.instagram_username}', '{photo.user.twitter_username}', '{photo.user.total_likes}', '{photo.user.total_photos}', '{photo.user.for_hire}', photos.photo_id)
                RETURNING user_id
            )

            INSERT INTO user_images(
                raw,
                small,
                regular,
                large,
                user_id
            ) VALUES ('{photo.user.profile_image.raw}', '{photo.user.profile_image.small}', '{photo.user.profile_image.regular}', '{photo.user.profile_image.large}', user_id)
            """
        self.db.execute(save_request_query)


def execute():
    settings = get_project_settings()
    collector_runner = CollectorRunner(settings)
    collector_runner.run()


if __name__ == "__main__":
    execute()
