from src.modules.measure_consumer.app.measure_consumer_controller import MeasureConsumerController
from src.modules.measure_consumer.app.measure_consumer_usecase import MeasureConsumerUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock

repo = Environments.get_producers_consumers_repo()()
usecase = MeasureConsumerUsecase(repo=repo)
controller = MeasureConsumerController(usecase=usecase)


def measure_consumer_presenter(request):
    request_data = request.body or dict(request.query_params)
    request = HttpRequest(body=dict(request_data))

    response = controller(request=request)

    return HttpResponse(body=response.body, status_code=response.status_code)
