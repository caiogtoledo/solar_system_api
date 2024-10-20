
from src.modules.get_actual_status_battery.app.get_actual_status_battery_controller import GetActualStatusBatteryController
from src.modules.get_actual_status_battery.app.get_actual_status_battery_usecase import GetActualStatusBatteryUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock

repo = Environments.get_battery_repo()()
usecase = GetActualStatusBatteryUsecase(repo=repo)
controller = GetActualStatusBatteryController(usecase=usecase)


def get_actual_status_battery_presenter(request):
    request_data = request.body or dict(request.query_params)
    request = HttpRequest(body=dict(request_data))

    response = controller(request=request)

    return HttpResponse(body=response.body, status_code=response.status_code)
