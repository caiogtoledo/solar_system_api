from pymongo import MongoClient
from src.shared.environments import Environments
from pymongo.errors import ConnectionFailure


class MongoDBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Iniciando conexão com o MongoDB")
            cls._instance = super().__new__(cls)
            MONGO_URI = Environments.get_envs().mongo_uri
            cls._instance.client = MongoClient(MONGO_URI)
            cls._instance.db = cls._instance.client[Environments.get_envs(
            ).mongo_db_name]
            cls._instance.validate_connection()
        return cls._instance

    def validate_connection(self):
        try:
            # Verificando se o servidor está acessível
            self.client.admin.command('ping')
            print("Conexão com o MongoDB foi bem-sucedida!")
        except ConnectionFailure:
            print("Falha ao conectar ao MongoDB.")
            raise

    def get_db(self):
        return self._instance.db
