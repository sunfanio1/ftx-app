from fastapi import APIRouter
from confluent_kafka import Consumer, Producer, KafkaException

router = APIRouter(prefix="/v1", tags=["Orders"])

config_producer = {
    'bootstrap.servers': 'kafka:9092'
}

config_consumer = {
    'bootstrap.servers': 'kafka:9092',  # Список серверов Kafka
    'group.id': 'mygroup',                  # Идентификатор группы потребителей
    'auto.offset.reset': 'earliest'         # Начальная точка чтения ('earliest' или 'latest')
}

@router.get("/orders/{order_id}")
async def get_user_order():
    return {"message": "Hello World"}

@router.get("/orders")
async def get_orders():

    return {"kafka_data": "message"}


@router.post("/orders")
async def create_order(data: str):
    producer = Producer(config_producer)
    producer.produce('test_topic', data)
    producer.flush()
    return {"message": data}

@router.patch("/orders/{order_id}")
async def change_order():
    return {"message": "Hello World"}

@router.delete("/orders/{order_id}")
async def delete_order():
    return {"message": "Hello World"}