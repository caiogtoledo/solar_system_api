from src.modules.get_actual_status_battery.app.get_actual_status_battery_controller import GetActualStatusBatteryController
from src.modules.get_actual_status_battery.app.get_actual_status_battery_usecase import GetActualStatusBatteryUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock


class Test_GetActualStatusBatteryControler:

    def test_get_actual_status_battery_controller(self):
        repo = BatteryRepositoryMock()
        usecase = GetActualStatusBatteryUsecase(repo=repo)
        controller = GetActualStatusBatteryController(usecase=usecase)

        test_id = "1"

        request = HttpRequest(body={
            'battery_id': test_id,
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['battery_id'] == test_id

        assert isinstance(response.body['soc'], float)
        assert isinstance(response.body['voltage'], float)
        assert isinstance(response.body['current'], float)
        assert isinstance(response.body['temperature'], float)
        assert isinstance(response.body['timestamp'], int)

        assert response.body['message'] == f"""this is the last status of battery: {
            test_id}"""

    def test_get_actual_status_battery_controller_missing_battery_id(self):
        repo = BatteryRepositoryMock()
        usecase = GetActualStatusBatteryUsecase(repo=repo)
        controller = GetActualStatusBatteryController(usecase=usecase)

        request = HttpRequest(body={
            # 'battery_id': '1',
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field battery_id is missing"
