
from src.modules.get_actual_status_battery.app.get_actual_status_battery_controller import GetActualStatusBatteryController
from src.modules.get_actual_status_battery.app.get_actual_status_battery_usecase import GetActualStatusBatteryUsecase
from src.modules.get_solar_panel_production.app.get_solar_panel_production_controller import GetSolarPanelProductionController
from src.modules.get_solar_panel_production.app.get_solar_panel_production_usecase import GetSolarPanelProductionUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock

repo = ProducersConsumersRepositoryMock()
usecase = GetSolarPanelProductionUsecase(repo=repo)
controller = GetSolarPanelProductionController(usecase=usecase)


def get_solar_panel_production_presenter(request):
    request_data = request.body or dict(request.query_params)
    request = HttpRequest(body=dict(request_data))

    response = controller(request=request)

    return HttpResponse(body=response.body, status_code=response.status_code)
