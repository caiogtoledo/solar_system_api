from src.modules.get_consumer_history.app.get_consumer_history_controller import GetConsumerHistoryController
from src.modules.get_producer_history.app.get_producer_history_controller import GetProducerHistoryController
from src.modules.get_producer_history.app.get_producer_history_usecase import GetProducerHistoryUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock


class Test_GetActualStatusBatteryControler:

    def test_get_producer_history_controller(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetProducerHistoryUsecase(repo=repo)
        controller = GetProducerHistoryController(usecase=usecase)

        test_id = "1"

        request = HttpRequest(body={
            'producer_id': test_id,
        })

        response = controller(request=request)

        assert response.status_code == 200

        for item in response.body["producer_history"]:
            assert item["producer_id"] == test_id

            assert isinstance(item['instantly'], float)
            assert isinstance(item['daily'], float)
            assert isinstance(item['monthly'], float)
            assert isinstance(item['timestamp'], int)

        assert response.body['message'] == f"""producer history"""

    def test_get_producer_history_controller_missing_solar_panel_id(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetProducerHistoryUsecase(repo=repo)
        controller = GetProducerHistoryController(usecase=usecase)

        request = HttpRequest(body={
            # 'producer_id': '1',
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field producer_id is missing"
