import random
from datetime import datetime, timedelta

from sqlalchemy.exc import SQLAlchemyError

from alpega.db.schema import TransportOrderAudit
from alpega.db.connection import create_database_connection
from alpega.models.transport_order_audit import TransportOrderAuditModel


def generate_test_data(db_session, num_records):
    try:
        for i in range(1, num_records + 1):
            order_id = random.randint(1, 100)
            customer_id = random.randint(1, 100)
            origin = f"Origin_{random.randint(1, 50)}"
            destination = f"Destination_{random.randint(1, 50)}"
            transport_status = random.choice(["Pending", "In Transit", "Delivered"])
            change_type = random.choice(["I", "U", "D"])
            change_timestamp = datetime.now() - timedelta(days=random.randint(1, 100))
            user_id = random.randint(1, 20)

            audit_data = TransportOrderAuditModel(
                order_id=order_id,
                customer_id=customer_id,
                origin=origin,
                destination=destination,
                transport_status=transport_status,
                change_type=change_type,
                change_timestamp=change_timestamp,
                user_id=user_id
            )

            db_audit_data = TransportOrderAudit(**audit_data.model_dump())
            db_session.add(db_audit_data)

        db_session.commit()
        print("Data inserted successfully.")

    except SQLAlchemyError as e:
        print(f"SQLAlchemy Error: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        db_session.close()
        


if __name__ == "__main__":
    db_session = create_database_connection()
    generate_test_data(db_session, 1000)
    db_session.close()


