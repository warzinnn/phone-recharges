from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "postgresql+psycopg2://warzin:my_pass@localhost:5432/recharges"
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        """Create an engine"""
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        """Returns engine"""
        return self.__engine

    def __enter__(self):
        """return self context"""
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

