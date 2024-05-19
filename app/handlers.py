import json

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from database import database
from utils import get_cached_aggregate
from models import AggregationRequest
import logging

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    logging.info('START logging')
    await message.answer("Welcome! Send me a JSON message with 'dt_from', 'dt_upto' and 'group_type' to get aggregated salary data.")

@router.message(Command('full'))
async def cmd_start(message: Message):
    collection = database.db.get_collection('salaries')
    documents = await collection.find().to_list(length=None)  # Получение всех документов
    response = "\n".join([str(doc) for doc in documents][:10])  # Преобразование документов в строку
    await message.answer(response)


@router.message(F.text)
async def process_message(message: Message):
    
    try:
        data = json.loads(message.text)
        request = AggregationRequest(**data)
        response = await get_cached_aggregate(request)
        await message.answer(response.model_dump_json())

    except Exception as e:
        await message.answer(f"Error: {str(e)}")


