
from src.modules.get_battery_prediction.app.get_battery_prediction_controller import GetBatteryPredictionController
from src.modules.get_battery_prediction.app.get_battery_prediction_usecase import GetBatteryPredictionUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse


producersConsumersRepo = Environments.get_producers_consumers_repo()()
batteryRepo = Environments.get_battery_repo()()
usecase = GetBatteryPredictionUsecase(
    producersConsumersRepo=producersConsumersRepo, batteryRepo=batteryRepo)
controller = GetBatteryPredictionController(usecase=usecase)


def get_battery_prediction_presenter(request):
    request_data = request.body or dict(request.query_params)
    request = HttpRequest(body=dict(request_data))

    response = controller(request=request)

    return HttpResponse(body=response.body, status_code=response.status_code)
