from typing import Optional
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from src.shared.domain.entities.measurement import Measurement
from src.shared.domain.repositories.measurements_repository_interface import IMeasurementsRepository
from src.shared.environments import Environments
from src.shared.infra.repositories.mongodb.mongodb_connection import MongoDBConnection


class MeasurementsRepositoryMongoDB(IMeasurementsRepository):
    def __init__(self):
        # print("Iniciando conexão com o MongoDB")
        # self.client = MongoClient(Environments.get_envs().mongo_uri)
        # self.db = self.client[Environments.get_envs().mongo_db_name]
        # DB_NAME = "measurements"
        # self.collection = self.db[DB_NAME]
        # self.validate_connection()

        db_manager = MongoDBConnection()
        self.collection = db_manager.get_db()["measurements"]

    def validate_connection(self):
        try:
            # Verificando se o servidor está acessível
            self.client.admin.command('ping')
            print("Conexão com o MongoDB foi bem-sucedida!")
        except ConnectionFailure:
            print("Falha ao conectar ao MongoDB.")
            raise

    def create_measure(self, measure: Measurement) -> None:
        self.collection.insert_one(measure.__dict__)

    def get_last_measure(self) -> Optional[Measurement]:
        # Ordena pelo timestamp em ordem decrescente e pega o primeiro documento
        document = self.collection.find().sort("timestamp", -1).limit(1)
        last_measurement = list(document)
        if last_measurement:
            last_measurement[0].pop("_id", None)  # Remove o campo _id
            return Measurement(**last_measurement[0])
        return None
