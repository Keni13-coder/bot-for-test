from aiocache import cached
from pymongo.errors import PyMongoError
from models import AggregationRequest, AggregationResponse
from database import database


@cached(ttl=300)
async def get_cached_aggregate(request: AggregationRequest) -> AggregationResponse:
    return await aggregate_salaries(request)

async def aggregate_salaries(request: AggregationRequest) -> AggregationResponse:
    try:
        collection = database.db.salaries

        pipeline = [
            {"$match": {
                "dt": {
                    "$gte": request.dt_from,
                    "$lte": request.dt_upto
                }
            }},
            {"$group": {
                "_id": get_group_stage(request.group_type),
                "total_value": {"$sum": "$value"}
            }},
            {"$sort": {"_id": 1}}
        ]

        cursor = collection.aggregate(pipeline)

        dataset = []
        labels = []
        async for doc in cursor:
            dataset.append(doc["total_value"])
            labels.append(doc["_id"])

        return AggregationResponse(dataset=dataset, labels=labels)

    except PyMongoError as e:
        raise ValueError(e)

def get_group_stage(group_type: str):
    if group_type == 'hour':
        return {
            "$dateToString": {
                "format": "%Y-%m-%dT%H:00:00",
                "date": "$dt"
            }
        }
    elif group_type == 'day':
        return {
            "$dateToString": {
                "format": "%Y-%m-%d",
                "date": "$dt"
            }
        }
    elif group_type == 'month':
        return {
            "$dateToString": {
                "format": "%Y-%m-%dT00:00:00",
                "date": {"$dateFromString": {"dateString": "$dt", "format": "%Y-%m-01T00:00:00"}}
            }
        }