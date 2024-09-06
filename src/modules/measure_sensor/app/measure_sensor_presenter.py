from src.modules.measure_sensor.app.measure_sensor_controller import MeasureSensorController
from src.modules.measure_sensor.app.measure_sensor_usecase import MeasureSensorUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.infra.repositories.measurements_repository_mock import MeasurementsRepositoryMock

repo = Environments.get_measurements_repo()()
usecase = MeasureSensorUsecase(repo=repo)
controller = MeasureSensorController(usecase=usecase)


def measure_sensor_presenter(request):
    request_data = request.body or dict(request.query_params)
    request = HttpRequest(body=dict(request_data))

    response = controller(request=request)

    return HttpResponse(body=response.body, status_code=response.status_code)
