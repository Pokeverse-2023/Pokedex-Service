from beanie import init_beanie
from motor import motor_asyncio

from app.config import Settings
from app.models import Pokemon


class Connect:
    def __init__(self):
        self.settings = Settings()

    async def start_connection(self):
        DB_NAME = self.settings.DB_NAME
        try:
            await init_beanie(
                database=self.get_client()[DB_NAME], document_models=[Pokemon]
            )
            print("Successful Connection To MongoDB")
        except Exception as exc:
            print(exc)

    def get_client(self):
        CONNECTION_URL = f"mongodb+srv://{self.settings.DB_USER}:{self.settings.DB_PASSWORD}@{self.settings.DB_URL}/{self.settings.DB_SETTINGS}"
        return motor_asyncio.AsyncIOMotorClient(CONNECTION_URL)
