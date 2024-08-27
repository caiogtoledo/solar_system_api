
from src.modules.create_alert.app.create_alert_controller import CreateAlertController
from src.modules.create_alert.app.create_alert_usecase import CreateAlertUsecase
from src.shared.infra.repositories.alerts_repository_mock import AlertsRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.infra.repositories.mongodb.alerts_repository_mongodb import AlertsRepositoryMongoDB

import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv('MONGO_URI')
db_name = str(os.getenv('DB_NAME'))
collection_name = "alerts"
print(f"URI: {uri}, DB_NAME: {db_name}, COLLECTION_NAME: {collection_name}")
repo = AlertsRepositoryMongoDB(
    uri=uri, db_name=db_name, collection_name=collection_name)

usecase = CreateAlertUsecase(repo=repo)
controller = CreateAlertController(usecase=usecase)


def create_alert_presenter(request):
    request_data = request.body
    request = HttpRequest(body=request_data)

    response = controller(request=request)

    return HttpResponse(body=response.body, status_code=response.status_code)
