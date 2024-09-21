from src.modules.get_consumer_history.app.get_consumer_history_controller import GetConsumerHistoryController
from src.modules.get_consumer_history.app.get_consumer_history_usecase import GetConsumerHistoryUsecase
from src.modules.get_status_battery_history.app.get_battery_status_history_controller import GetBatteryStatusHistoryController
from src.modules.get_status_battery_history.app.get_battery_status_history_usecase import GetBatteryStatusHistoryUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock
from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock


class Test_GetActualStatusBatteryControler:

    def test_get_consumer_history_controller(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetConsumerHistoryUsecase(repo=repo)
        controller = GetConsumerHistoryController(usecase=usecase)

        test_id = "1"

        request = HttpRequest(body={
            'consumer_id': test_id,
        })

        response = controller(request=request)

        assert response.status_code == 200

        for item in response.body["consumer_history"]:
            assert item["consumer_id"] == test_id

            assert isinstance(item['instantly'], float)
            assert isinstance(item['daily'], float)
            assert isinstance(item['monthly'], float)
            assert isinstance(item['timestamp'], int)

        assert response.body['message'] == f"""Consumer history"""

    def test_get_battery_status_history_controller_missing_battery_id(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetConsumerHistoryUsecase(repo=repo)
        controller = GetConsumerHistoryController(usecase=usecase)

        request = HttpRequest(body={
            # 'consumer_id': '1',
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field consumer_id is missing"
