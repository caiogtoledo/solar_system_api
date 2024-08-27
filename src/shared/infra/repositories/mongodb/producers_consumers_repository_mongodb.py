from typing import List, Optional
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from src.shared.domain.entities.solar_panel import SolarPanel
from src.shared.domain.entities.consumer import Consumer
from src.shared.domain.repositories.producers_consumers_repository_interface import IProducersConsumersRepository


class ProducersConsumersRepositoryMongoDB(IProducersConsumersRepository):
    def __init__(self, uri: str, db_name: str, collection_name: str):
        print("Iniciando conexão com o MongoDB")
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.validate_connection()

    def validate_connection(self):
        try:
            # Verificando se o servidor está acessível
            self.client.admin.command('ping')
            print("Conexão com o MongoDB foi bem-sucedida!")
        except ConnectionFailure:
            print("Falha ao conectar ao MongoDB.")
            raise

    def create_solar_panel_measure(self, measure: SolarPanel) -> None:
        # Adiciona um campo 'type' para diferenciar entre SolarPanel e Consumer
        measure_dict = measure.__dict__.copy()
        measure_dict["type"] = "solar_panel"
        self.collection.insert_one(measure_dict)

    def create_consumer_measure(self, measure: Consumer) -> None:
        # Adiciona um campo 'type' para diferenciar entre SolarPanel e Consumer
        measure_dict = measure.__dict__.copy()
        measure_dict["type"] = "consumer"
        self.collection.insert_one(measure_dict)

    def get_last_solar_panel_measure(self, solar_panel_id: str) -> Optional[SolarPanel]:
        # Filtra pelo id e pelo type
        document = self.collection.find(
            {"solar_panel_id": solar_panel_id, "type": "solar_panel"}).sort("timestamp", -1).limit(1)
        last_measurement = list(document)
        if last_measurement:
            last_measurement[0].pop("_id", None)
            return SolarPanel(**last_measurement[0])
        return None

    def get_last_consumer_measure(self, consumer_id: str) -> Optional[Consumer]:
        # Filtra pelo id e pelo type
        document = self.collection.find(
            {"consumer_id": consumer_id, "type": "consumer"}).sort("timestamp", -1).limit(1)
        last_measurement = list(document)
        if last_measurement:
            last_measurement[0].pop("_id", None)
            return Consumer(**last_measurement[0])
        return None
