from src.modules.measure_battery.app.measure_battery_controller import MeasureBatteryController
from src.modules.measure_battery.app.measure_battery_usecase import MeasureBatteryUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock


class Test_CreateUserControler:
    def test_measurement_battery_controller(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo=repo)
        controller = MeasureBatteryController(usecase=usecase)

        request = HttpRequest(body={
            'battery_id': '1',
            'soc': 0.5,
            'voltage': 3.7,
            'current': 0.1,
            'temperature': 25.0
        })

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['battery_id'] == repo.battery_measurements[-1].battery_id
        assert response.body['soc'] == repo.battery_measurements[-1].soc
        assert response.body['voltage'] == repo.battery_measurements[-1].voltage
        assert response.body['current'] == repo.battery_measurements[-1].current
        assert response.body['temperature'] == repo.battery_measurements[-1].temperature
        assert response.body['message'] == "the measure was created successfully"

    def test_create_user_controller_missing_battery_id(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo=repo)
        controller = MeasureBatteryController(usecase=usecase)

        request = HttpRequest(body={
            'email': '21.01444-2@maua.br'})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field name is missing"

    def test_create_user_controller_missing_soc(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo=repo)
        controller = MeasureBatteryController(usecase=usecase)

        request = HttpRequest(body={
            'name': 'Branco do Branco Branco da Silva'})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field email is missing"

    def test_create_user_controller_invalid_email(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo=repo)
        controller = CreateUserController(usecase=usecase)

        request = HttpRequest(body={
            'name': 'Branco do Branco Branco da Silva',
            'email': 'branco@branco'})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field email is not valid"

    def test_create_user_controller_invalid_name(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo=repo)
        controller = CreateUserController(usecase=usecase)

        request = HttpRequest(body={
            'name': 'B',
            'email': 'branco@branco.com'})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field name is not valid"
