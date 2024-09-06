from src.modules.measure_solar_panel.app.measure_solar_panel_controller import MeasureSolarPanelController
from src.modules.measure_solar_panel.app.measure_solar_panel_usecase import MeasureSolarPanelUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock

repo = Environments.get_producers_consumers_repo()()
usecase = MeasureSolarPanelUsecase(repo=repo)
controller = MeasureSolarPanelController(usecase=usecase)


def measure_solar_panel_presenter(request):
    request_data = request.body or dict(request.query_params)
    request = HttpRequest(body=dict(request_data))

    response = controller(request=request)

    return HttpResponse(body=response.body, status_code=response.status_code)
