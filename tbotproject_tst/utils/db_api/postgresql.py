import sqlite3
import asyncio
from data import config

import asyncpg as asyncpg

class Database:
    def init(self):
        loop = asyncio.get_event_loop()
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PGUSER,
                database=config.DBNAME,
                password=config.PGPASSWORD,
                host=config.IP,
                port=config.DBPORT
            )
        ).connection.cursor()