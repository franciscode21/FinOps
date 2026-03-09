import uuid

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class CloudResource(Base):
    __tablename__ = "cloud_resources"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cloud_account_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("cloud_accounts.id", ondelete="CASCADE"), nullable=False
    )
    cloud_service_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("cloud_services.id", ondelete="RESTRICT"), nullable=False
    )
    resource_external_id: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    resource_type: Mapped[str] = mapped_column(String(128), nullable=False)
    region: Mapped[str | None] = mapped_column(String(64), nullable=True)

    cloud_account = relationship("CloudAccount", back_populates="resources")
    cloud_service = relationship("CloudService", back_populates="resources")
