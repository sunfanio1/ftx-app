from random import random
from typing import Annotated

from fastapi import APIRouter, Response, Depends


from src.models.orders import OrdersRequest
from src.services import orders
from fastapi import status

router = APIRouter(prefix="/v1", tags=["Orders"])

# config_producer = {
#     'bootstrap.servers': 'kafka:9092'
# }
#
# config_consumer = {
#     'bootstrap.servers': 'kafka:9092',  # Список серверов Kafka
#     'group.id': 'mygroup',                  # Идентификатор группы потребителей
#     'auto.offset.reset': 'earliest'         # Начальная точка чтения ('earliest' или 'latest')
# }

OrdersService = Annotated[orders.OrdersService, Depends()]

@router.get("/orders/{order_id}")
async def get_user_order():
    return {"message": "Hello World"}

@router.get("/orders")
async def get_orders():

    if random() < 0.5:
        return Response(status_code=500)

    return {"kafka_data": "message"}


@router.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_order(order_data: OrdersRequest, service: OrdersService):
    """Создать заказ на поездку"""
    await service.create(order_data)
    return {"message": order_data.model_dump()}

@router.patch("/orders/{order_id}")
async def change_order():
    return {"message": "Hello World"}

@router.delete("/orders/{order_id}")
async def delete_order():
    return {"message": "Hello World"}