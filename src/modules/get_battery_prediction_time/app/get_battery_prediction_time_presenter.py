from src.modules.get_battery_prediction_time.app.get_battery_prediction_time_controller import GetBatteryPredictionTimeController
from src.modules.get_battery_prediction_time.app.get_battery_prediction_time_usecase import GetBatteryPredictionTimeUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse


producersConsumersRepo = Environments.get_producers_consumers_repo()()
batteryRepo = Environments.get_battery_repo()()
usecase = GetBatteryPredictionTimeUsecase(
    producersConsumersRepo=producersConsumersRepo, batteryRepo=batteryRepo)
controller = GetBatteryPredictionTimeController(usecase=usecase)


def get_battery_prediction_time_presenter(request):
    request_data = request.body or dict(request.query_params)
    request = HttpRequest(body=dict(request_data))

    response = controller(request=request)

    return HttpResponse(body=response.body, status_code=response.status_code)
