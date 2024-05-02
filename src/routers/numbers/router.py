from fastapi import APIRouter, Body, Query, status
from fastapi_cache.decorator import cache
from typing import Annotated, Any

from redis_db.manager import redis
from .schemas import PhoneData, FullData
from core import BaseResponse, BaseHTTPException


router: APIRouter = APIRouter(
    tags=['Redis']
)

@router.post('/write_data', response_model=BaseResponse[FullData])
async def write_data(data: FullData = Body(embed=True)):
    response: bool = await redis.set(name=data.phone, value=data.address, ex=30)
    if response:
        return BaseResponse(status='success', data=data)
    

@router.get('/check_data',  response_model=BaseResponse[FullData])
async def check_data(phone = Query(PhoneData)):
    response: Any = await redis.get(name=phone)
    print(response)
    if response:
        return BaseResponse(status='success', data=FullData(phone=phone, address=response))
    else:
        raise BaseHTTPException(status_code=status.HTTP_400_BAD_REQUEST, msg='Phone not found')