
from src.modules.get_status_battery_history.app.get_battery_status_history_controller import GetBatteryStatusHistoryController
from src.modules.get_status_battery_history.app.get_battery_status_history_usecase import GetBatteryStatusHistoryUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock
from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock

repo = Environments.get_battery_repo()()
usecase = GetBatteryStatusHistoryUsecase(repo=repo)
controller = GetBatteryStatusHistoryController(usecase=usecase)


def get_battery_status_history_presenter(request):
    request_data = request.body or dict(request.query_params)
    request = HttpRequest(body=dict(request_data))

    response = controller(request=request)

    return HttpResponse(body=response.body, status_code=response.status_code)
