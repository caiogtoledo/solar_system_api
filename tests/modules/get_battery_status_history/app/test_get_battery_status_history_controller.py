from src.modules.get_status_battery_history.app.get_battery_status_history_controller import GetBatteryStatusHistoryController
from src.modules.get_status_battery_history.app.get_battery_status_history_usecase import GetBatteryStatusHistoryUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock


class Test_GetActualStatusBatteryControler:

    def test_get_battery_status_history_controller(self):
        repo = BatteryRepositoryMock()
        usecase = GetBatteryStatusHistoryUsecase(repo=repo)
        controller = GetBatteryStatusHistoryController(usecase=usecase)

        test_id = "1"

        request = HttpRequest(body={
            'battery_id': test_id,
        })

        response = controller(request=request)

        assert response.status_code == 200

        for status in response.body["battery_status_history"]:
            assert status["battery_id"] == test_id

            assert isinstance(status['soc'], float)
            assert isinstance(status['voltage'], float)
            assert isinstance(status['current'], float)
            assert isinstance(status['temperature'], float)
            assert isinstance(status['timestamp'], int)

        assert response.body['message'] == f"""Status battery history"""

    def test_get_battery_status_history_controller_missing_battery_id(self):
        repo = BatteryRepositoryMock()
        usecase = GetBatteryStatusHistoryUsecase(repo=repo)
        controller = GetBatteryStatusHistoryController(usecase=usecase)

        request = HttpRequest(body={
            # 'battery_id': '1',
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field battery_id is missing"
