from typing import List, Optional
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from src.shared.domain.entities.alert import Alert
from src.shared.domain.repositories.alerts_repository_interface import IAlertsRepository


class AlertsRepositoryMongoDB(IAlertsRepository):
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

    def create_alert(self, alert: Alert) -> Alert:
        self.collection.insert_one(alert.__dict__)
        return alert

    def get_all_alerts(self) -> List[Alert]:
        documents = self.collection.find()
        alerts = []
        for document in documents:
            # Remove o campo _id que é gerado automaticamente pelo MongoDB
            document.pop("_id", None)
            alerts.append(Alert(**document))
        return alerts

    def update_alert(self, alert: Alert) -> Alert:
        # Atualizando o alerta com o mesmo alert_id
        self.collection.update_one(
            {"alert_id": alert.alert_id},
            {"$set": alert.__dict__}
        )
        return alert

    def get_alert_by_id(self, alert_id: str) -> Optional[Alert]:
        document = self.collection.find_one({"alert_id": alert_id})
        if document:
            document.pop("_id", None)  # Remove o campo _id
            return Alert(**document)
        return None
