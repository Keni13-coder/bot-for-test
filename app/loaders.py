import bson

from database import database

async def load_initial_data():
    collection = database.db.salaries
    if await collection.estimated_document_count() == 0:
        with open('./data/sample_collection.bson', 'rb') as f:
            data = bson.decode_all(f.read())
            await collection.insert_many(data)