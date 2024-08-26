from src.modules.measure_battery.app.measure_battery_controller import MeasureBatteryController
from src.modules.measure_battery.app.measure_battery_usecase import MeasureBatteryUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock

repo = BatteryRepositoryMock()
usecase = MeasureBatteryUsecase(repo=repo)
controller = MeasureBatteryController(usecase=usecase)


def measure_battery_presenter(request):
    request_data = request.body or dict(request.query_params)
    request = HttpRequest(body=dict(request_data))

    response = controller(request=request)

    return HttpResponse(body=response.body, status_code=response.status_code)
