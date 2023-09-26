from sqlalchemy import CHAR, TIMESTAMP, Column, Enum, Index, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text

Base = declarative_base()


class TransportOrder(Base):
    __tablename__ = "transport_order"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer)
    origin = Column(String(100))
    destination = Column(String(100))
    transport_status = Column(
        Enum("Pending", "In Transit", "Delivered", name="transport_status_enum"),
        nullable=False,
    )


class TransportOrderAudit(Base):
    __tablename__ = "transport_order_audit"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, nullable=False)
    customer_id = Column(Integer, nullable=False)
    origin = Column(String(100), nullable=False)
    destination = Column(String(100), nullable=False)
    transport_status = Column(
        Enum("Pending", "In Transit", "Delivered", name="transport_status_enum"),
        nullable=False,
    )
    change_type = Column(CHAR(1), nullable=False, server_default=text("'I'"))
    change_timestamp = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    user_id = Column(Integer, nullable=False)


Index("idx_transport_order_audit_order_id", TransportOrderAudit.order_id)
Index("idx_transport_order_audit_customer_id", TransportOrderAudit.customer_id)
