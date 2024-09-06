
from src.modules.get_all_alerts.app.get_all_alerts_controller import GetAllAlertsController
from src.modules.get_all_alerts.app.get_all_alerts_usecase import GetAllAlertsUsecase
from src.shared.environments import Environments
from src.shared.infra.repositories.alerts_repository_mock import AlertsRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse

repo = Environments.get_alerts_repo()()
usecase = GetAllAlertsUsecase(repo=repo)
controller = GetAllAlertsController(usecase=usecase)


def get_all_alerts_presenter(request):
    request = HttpRequest(body={})

    response = controller(request=request)

    return HttpResponse(body=response.body, status_code=response.status_code)
