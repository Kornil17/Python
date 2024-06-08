import asyncpg
import asyncio
from loguru import logger
from typing import List, Tuple, Union
from random import sample


def commands():
    CREATE_BRAND_TABLE = \
        """
        CREATE TABLE IF NOT EXISTS brand(
        brand_id SERIAL PRIMARY KEY,
        brand_name TEXT NOT NULL
        );"""

    CREATE_PRODUCT_TABLE = \
        """
        CREATE TABLE IF NOT EXISTS product(
        product_id SERIAL PRIMARY KEY,
        product_name TEXT NOT NULL,
        brand_id INT NOT NULL,
        FOREIGN KEY (brand_id) REFERENCES brand(brand_id)
        );"""

    CREATE_PRODUCT_COLOR_TABLE = \
        """
        CREATE TABLE IF NOT EXISTS product_color(
        product_color_id SERIAL PRIMARY KEY,
        product_color_name TEXT NOT NULL
        );"""

    CREATE_PRODUCT_SIZE_TABLE = \
        """
        CREATE TABLE IF NOT EXISTS product_size(
        product_size_id SERIAL PRIMARY KEY,
        product_size_name TEXT NOT NULL
        );"""

    CREATE_SKU_TABLE = \
        """
        CREATE TABLE IF NOT EXISTS sku(
        sku_id SERIAL PRIMARY KEY,
        product_id INT NOT NULL,
        product_size_id INT NOT NULL,
        product_color_id INT NOT NULL,
        FOREIGN KEY (product_id)
        REFERENCES product(product_id),
        FOREIGN KEY (product_size_id)
        REFERENCES product_size(product_size_id),
        FOREIGN KEY (product_color_id)
        REFERENCES product_color(product_color_id)
        );"""

    COLOR_INSERT = \
        """
        INSERT INTO product_color VALUES(1, 'Blue');
        INSERT INTO product_color VALUES(2, 'Black');
        """

    SIZE_INSERT = \
        """
        INSERT INTO product_size VALUES(1, 'Small');
        INSERT INTO product_size VALUES(2, 'Medium');
        INSERT INTO product_size VALUES(3, 'Large');
        """
    ALL_BRAND_DATA = \
        """
        SELECT * FROM brand;
        """
    return [CREATE_BRAND_TABLE,
            CREATE_PRODUCT_TABLE,
            CREATE_PRODUCT_COLOR_TABLE,
            CREATE_PRODUCT_SIZE_TABLE,
            CREATE_SKU_TABLE,
            SIZE_INSERT,
            COLOR_INSERT]


async def execute_sql_commands(connection):
    statements = commands()
    print('Создается база данных product...')
    for statement in statements:
        status = await connection.execute(statement)
    print(status)
    print("База данных product")


async def execute_custom_query(query, **kwargs):
    try:
        connection = await asyncpg.connect(**kwargs)
        id = await connection.execute(query)
        logger.debug(id)
    except Exception as error:
        logger.error("Error", exc_info=error)


async def fetch_custom_query(query, **kwargs):
    try:
        connection = await asyncpg.connect(**kwargs)
        id = await connection.fetch(query)
        logger.debug(f"Get data {id}")
    except Exception as error:
        logger.error("Error", exc_info=error)


async def fetch_custom_query2(pool):
    try:
        async with pool.acquire() as connection:
            id = await connection.fetch("SELECT * FROM brand;")
        logger.debug(f"Get data {id}")
    except Exception as error:
        logger.error("Error", exc_info=error)


def load_common_words() -> List[str]:
    with open('./common_words.txt') as common_words:
        return common_words.readlines()


def generate_brand_names(words: List[str]) -> List[Tuple[Union[str,]]]:
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_brands = "INSERT INTO brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_brands, brands)


async def main_marks():
    common_words = load_common_words()
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5000,
                                       user='test',
                                       database='postgres',
                                       password='1234567890')
    await insert_brands(common_words, connection)


async def creating_pool(**kwargs):
    async with asyncpg.create_pool(**kwargs, min_size=6, max_size=6) as pool:
        await asyncio.gather(*[fetch_custom_query2(pool), fetch_custom_query2(pool)])


async def transaction_func():
    connection = await asyncpg.connect(host='localhost',
                                       port=5000,
                                       user='test',
                                       database='postgres',
                                       password='1234567890')
    transaction = connection.transaction()
    await transaction.start()
    try:
        await connection.execute("INSERT INTO product_color VALUES(3, 'Yellow');")
    except asyncpg.PostgresError as error:
        print(f"Произошла ошибка, откат транзакции -> {error}")
        await transaction.rollback()
    else:
        print("Запись вставлена успешно!!")
        await transaction.commit()

async def cursor_func():
    connection = await asyncpg.connect(host='localhost',
                                       port=5000,
                                       user='test',
                                       database='postgres',
                                       password='1234567890')
    async with connection.transaction():
        cursor = await connection.cursor("select * from brand;")
        await cursor.forward(101)
        brand = await cursor.fetch(100)
        for b in brand:
            print(b)
    await connection.close()
async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count > to_take - 1:
            return
        item_count = item_count + 1
        yield item

async def limit_generator():
    connection = await asyncpg.connect(host='localhost',
                                       port=5000,
                                       user='test',
                                       database='postgres',
                                       password='1234567890')
    async with connection.transaction():
        cursor = connection.cursor("select * from brand;")
        async for b in take(cursor, 5):
            print(b)
    await connection.close()
async def main():
    connection = await asyncpg.connect(host='localhost',
                                       port=5000,
                                       user='test',
                                       database='postgres',
                                       password='1234567890')
    version = connection.get_server_version()
    print(f'Подключено! Версия Postgres равна {version}')
    await execute_sql_commands(connection)
    await connection.close()


# asyncio.run(main())
# asyncio.run(execute_custom_query("select * from brand;",
#                                  host='localhost',
#                                  port=5000,
#                                  user='test',
#                                  database='postgres',
#                                  password='1234567890'))
# asyncio.run(fetch_custom_query("select * from brand;",
#                                host='localhost',
#                                port=5000,
#                                user='test',
#                                database='postgres',
#                                password='1234567890'))
# asyncio.run(main_marks())
# asyncio.run(creating_pool(host='localhost',
#                           port=5000,
#                           user='test',
#                           database='postgres',
#                           password='1234567890'))

# asyncio.run(transaction_func())
# asyncio.run(cursor_func())
asyncio.run(limit_generator())