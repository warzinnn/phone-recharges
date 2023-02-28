class EntityAlreadyExists(Exception):
    """duplicate key value violates unique constraint"""

    pass

class DataIsNotPresentInTable(Exception):
    """IntegrityError: (psycopg2.errors.ForeignKeyViolation)"""

    pass
