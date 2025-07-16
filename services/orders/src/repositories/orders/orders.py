import uuid
from typing import Any
from uuid import uuid3

from src.repositories.tables.orders import Orders
from sqlalchemy.orm import Session

class OrdersRepository:
    """Слой репозитория для работы с сущностями Заказов на уровне БД"""

    table = Orders.__table__


    def __init__(self, db: Session):
        self.db = db


    def create(self, order_data: dict[Any, Any]):
        print("order data", order_data)
        order = Orders(user_id = uuid.uuid4(),
                       destination_from = f"POINT({order_data['destination_from']['lat']} { 
                       order_data['destination_from']['lon']})",
                       destination_to = f"POINT({order_data['destination_to']['lat']} { 
                       order_data['destination_to']['lon']})")

        self.db.add(order)
        self.db.commit()

    def dict_to_ewkt(self, point_dict):
        return f"POINT({point_dict['lon']} {point_dict['lat']})"