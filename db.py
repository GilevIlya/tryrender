import asyncio
import asyncpg
import json

import os
from dotenv import load_dotenv, find_dotenv

find_path = find_dotenv()
load_dotenv(find_path)


CONNECTION = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "host": os.getenv("DB_HOST")
}
if CONNECTION is None:
    raise ValueError("CONNECTION не задана в .env файле!")

async def validation(id):
    try:
        conn = await asyncpg.connect(**CONNECTION)
        get_inf = await conn.fetchrow('SELECT clients.id FROM clients WHERE id=$1', id)
        return get_inf is not None
    finally:
        await conn.close()

async def reg_acc(id, name, age):
    try:
        conn = await asyncpg.connect(**CONNECTION)
        reg_account = await conn.execute("INSERT INTO clients (id, first_name, username) VALUES ($1, $2, $3)", int(id), name, int(age))
    finally:
        await conn.close()

async def get_city_and_coords(user_id: int):
    conn = await asyncpg.connect(**CONNECTION)
    try:
        res = await conn.fetchrow(
            "SELECT cityandcoords FROM clients WHERE id=$1", user_id
        )
        city = json.loads(res['cityandcoords'])
        print(city['lon'])
    finally:
        await conn.close()

res = asyncio.run(get_city_and_coords(1441142423))
print(res)