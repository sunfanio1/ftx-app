from fastapi import Depends
from src.models.orders import OrdersRequest

from src.dependencies.depedencies import get_orders_repository
from src.repositories.orders.orders import OrdersRepository


class OrdersService:
    """ Сервисный слой для работы с Заказами пользователя"""

    def __init__(self, repository: OrdersRepository = Depends(get_orders_repository)) -> None:

        self.repository = repository

    async def create(self, order_data: OrdersRequest):

        self.repository.create(order_data.model_dump())

        return True
