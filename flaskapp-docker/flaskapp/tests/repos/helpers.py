from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import CompileError


def get_in_memory_database(tables=None):
    """Create an in-memory sqlalchemy session for use in tests.

    Ideally we would use the same database type as our main database store in
    production (MySQL) rather than SQLite so for full integration tests or
    MySQL specific tests you may need to consider this.

    Example Usage:
        >> from warehouse.tests.repos.helpers import get_in_memory_database
        >> from lib.storage.models import Purchase
        >> from lib.storage.models import Pallet
        >>
        >> # Get the database session, creating only the required tables.
        >> db = get_in_memory_database(tables=[Purchase, Pallet])
        >>
        >> # Add some Purchases for testing.
        >> db.add(Purchase(purchase_id=1, order_number='PO0001')
        >> db.add(Purchase(purchase_id=2, order_number='PO0002')
        >>
        >> # Add some Pallets for testing.
        >> db.add(Pallet(pallet_id=1, status=Pallet.STATUS_GOOD)
        >> db.add(Pallet(pallet_id=2, status=Pallet.STATUS_QC)

    Args:
        tables (list): List of lib.storage.model classes to create tables for.

    Returns:
        obj: sqlalchemy session object.
    """
    engine = create_engine('sqlite://')

    session = sessionmaker()
    session.configure(bind=engine)
    session = session()
    session._model_changes = {}

    if tables:
        for table in tables:
            table.metadata.create_all(engine)

    return session


def create_in_memory_database(data):
    """
    Create an in-memory database populated with data.
    :param dict data: Data to populate for each model (Model: [list of dicts])
    :return: Database session object
    """
    db = get_in_memory_database(tables=data.keys())

    # Populate the database with the passed model data.
    [
        db.add(model(**record))
        for model, records in data.items()
        for record in records
    ]

    # BaseRepository functions will auto-flush data added to the
    # database during the session, so queries would return results even
    # if the data was not committed. To use non-BaseRepository queries
    # on the in-memory database, an explicit commit is required.
    db.commit()

    return db
