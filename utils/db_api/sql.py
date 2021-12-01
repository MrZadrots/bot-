import asyncio
import asyncpg
import logging

from data.config import PG_PASSWORD,PG_USER,HOST
#from config import PG_PASSWORD,PG_USER,HOST
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    # level=logging.DEBUG,  # Можно заменить на другой уровень логгирования.
                    )

async def create_db():
    create_db_command = open("E:\\bots\\bot-\\utils\\db_api\\create_db.sql", "r").read()
    
    logging.info('Connecting to DB')
    conn:asyncpg.Connection = await asyncpg.connect(
        user = PG_USER,
        password = PG_PASSWORD,
        host = HOST,
    )
    await conn.execute(create_db_command)
    await conn.close()
    logging.info("table has been created")


async def create_pool():
    result = await asyncpg.create_pool(
        user = PG_USER,
        password = PG_PASSWORD,
        host = HOST
    )
    return result


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
