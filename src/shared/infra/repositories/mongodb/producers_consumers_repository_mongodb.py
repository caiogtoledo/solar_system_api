from typing import Optional, List
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from src.shared.domain.entities.solar_panel import SolarPanel
from src.shared.domain.entities.consumer import Consumer
from src.shared.domain.repositories.producers_consumers_repository_interface import IProducersConsumersRepository
from src.shared.environments import Environments
from src.shared.infra.repositories.mongodb.mongodb_connection import MongoDBConnection


class ProducersConsumersRepositoryMongoDB(IProducersConsumersRepository):
    def __init__(self):
        db_manager = MongoDBConnection()
        self.collection = db_manager.get_db()["producers_consumers"]

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
            last_measurement[0].pop("type", None)
            return SolarPanel(**last_measurement[0])
        return None

    def get_last_consumer_measure(self, consumer_id: str) -> Optional[Consumer]:
        # Filtra pelo id e pelo type
        document = self.collection.find(
            {"consumer_id": consumer_id, "type": "consumer"}).sort("timestamp", -1).limit(1)
        last_measurement = list(document)
        if last_measurement:
            last_measurement[0].pop("_id", None)
            last_measurement[0].pop("type", None)
            return Consumer(**last_measurement[0])
        return None

    def get_solar_panel_measurements(self, solar_panel_id: str) -> List[SolarPanel]:
        # Filtra pelo id e pelo type
        documents = self.collection.find(
            {"solar_panel_id": solar_panel_id, "type": "solar_panel"}).sort("timestamp", -1)
        measurements = []
        for document in documents:
            document.pop("_id", None)
            document.pop("type", None)
            measurements.append(SolarPanel(**document))
        return measurements

    def get_all_solar_panels_measurements(self, records: int = None) -> List[SolarPanel]:
        # Retorna todos os painéis solares ou os últimos 'records' registros
        query = {"type": "solar_panel"}
        documents = self.collection.find(query).sort("timestamp", -1)
        if records:
            documents = documents.limit(records)

        measurements = []
        for document in documents:
            document.pop("_id", None)
            document.pop("type", None)
            measurements.append(SolarPanel(**document))
        return measurements

    def get_consumer_measurements(self, consumer_id: str) -> List[Consumer]:
        # Filtra pelo id e pelo type
        documents = self.collection.find(
            {"consumer_id": consumer_id, "type": "consumer"}).sort("timestamp", -1)
        measurements = []
        for document in documents:
            document.pop("_id", None)
            document.pop("type", None)
            measurements.append(Consumer(**document))
        return measurements

    def get_all_consumers_measurements(self, records: int = None) -> List[Consumer]:
        # Retorna todos os consumidores ou os últimos 'records' registros
        query = {"type": "consumer"}
        documents = self.collection.find(query).sort("timestamp", -1)

        if records != None:
            documents = documents.limit(records)

        measurements = []
        for document in documents:
            document.pop("_id", None)
            document.pop("type", None)
            measurements.append(Consumer(**document))
        return measurements
