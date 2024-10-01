
from src.modules.get_producer_history.app.get_producer_history_controller import GetProducerHistoryController
from src.modules.get_producer_history.app.get_producer_history_usecase import GetProducerHistoryUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse


repo = Environments.get_producers_consumers_repo()()
usecase = GetProducerHistoryUsecase(repo=repo)
controller = GetProducerHistoryController(usecase=usecase)


def get_producer_history_presenter(request):
    request_data = request.body or dict(request.query_params)
    request = HttpRequest(body=dict(request_data))

    response = controller(request=request)

    return HttpResponse(body=response.body, status_code=response.status_code)
