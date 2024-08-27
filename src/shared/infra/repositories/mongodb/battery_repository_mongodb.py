from typing import List, Optional
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from src.shared.domain.entities.battery import Battery
from src.shared.domain.repositories.battery_repository_interface import IBatteryRepository


class BatteryRepositoryMongoDB(IBatteryRepository):
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

    def create_measure(self, new_measurement: Battery) -> Battery:
        self.collection.insert_one(new_measurement.__dict__)
        return new_measurement

    def get_all_battery_measurements(self, battery_id: str) -> Optional[List[Battery]]:
        documents = self.collection.find({"battery_id": battery_id})
        measurements = []
        for document in documents:
            # Remove o campo _id que é gerado automaticamente pelo MongoDB
            document.pop("_id", None)
            measurements.append(Battery(**document))

        if not measurements:
            return None
        return sorted(measurements, key=lambda bat: bat.timestamp)

    def get_last_battery_measurement_by_id(self, battery_id: str) -> Optional[Battery]:
        document = self.collection.find(
            {"battery_id": battery_id}).sort("timestamp", -1).limit(1)
        last_measurement = list(document)
        if last_measurement:
            last_measurement[0].pop("_id", None)  # Remove o campo _id
            return Battery(**last_measurement[0])
        return None
