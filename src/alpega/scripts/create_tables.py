from alpega.db.schema import Base
from alpega.db.connection import create_database_connection
import traceback

if __name__ == "__main__":
    try:
        db_session = create_database_connection()
        Base.metadata.create_all(db_session.bind)

        db_session.close()
        print("Database schema created successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        traceback.print_exc() 
