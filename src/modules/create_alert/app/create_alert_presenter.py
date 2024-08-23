
from src.modules.create_alert.app.create_alert_controller import CreateAlertController
from src.modules.create_alert.app.create_alert_usecase import CreateAlertUsecase
from src.shared.infra.repositories.alerts_repository_mock import AlertsRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

repo = AlertsRepositoryMock()
usecase = CreateAlertUsecase(repo=repo)
controller = CreateAlertController(usecase=usecase)


def create_alert_presenter(request):
    request_data = request.get_json()
    request = HttpRequest(body=request_data)

    response = controller(request=request)

    return response.body, response.status_code
