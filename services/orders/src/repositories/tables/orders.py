from datetime import UTC, datetime
from uuid import UUID

from sqlalchemy import Uuid, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from geoalchemy2 import Geometry

from services.orders.src.repositories.tables.base import Base


class Orders(Base):
    """ Модель заказов поездок пользователя"""

    __tablename__ = "orders"

    user_id: Mapped[UUID] = mapped_column(Uuid, nullable=False)

    destination_from: Mapped[Geometry] = mapped_column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    destination_to: Mapped[Geometry | None] = mapped_column(Geometry(geometry_type='POINT', srid=4326), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now(UTC))
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True, onupdate=datetime.now(UTC))
    finished_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
