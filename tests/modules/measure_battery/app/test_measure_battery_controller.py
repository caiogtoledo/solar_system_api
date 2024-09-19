from src.modules.measure_battery.app.measure_battery_controller import MeasureBatteryController
from src.modules.measure_battery.app.measure_battery_usecase import MeasureBatteryUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock
import datetime


class Test_MeasureBatteryControler:
    def test_measurement_battery_controller(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo=repo)
        controller = MeasureBatteryController(usecase=usecase)

        request = HttpRequest(body={
            'battery_id': '1',
            'soc': 0.5,
            'voltage': 3.7,
            'current': 0.1,
            'temperature': 25.0,
            'timestamp': int(datetime.datetime.now().timestamp())*1000
        })

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['battery_id'] == repo.battery_measurements[-1].battery_id
        assert response.body['soc'] == repo.battery_measurements[-1].soc
        assert response.body['voltage'] == repo.battery_measurements[-1].voltage
        assert response.body['current'] == repo.battery_measurements[-1].current
        assert response.body['temperature'] == repo.battery_measurements[-1].temperature
        assert response.body['timestamp'] == repo.battery_measurements[-1].timestamp
        assert response.body['message'] == "the measure was created successfully"

    def test_create_user_controller_missing_battery_id(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo=repo)
        controller = MeasureBatteryController(usecase=usecase)

        request = HttpRequest(body={
            # 'battery_id': '1',
            'soc': 0.5,
            'voltage': 3.7,
            'current': 0.1,
            'temperature': 25.0,
            'timestamp': int(datetime.datetime.now().timestamp())*1000
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field battery_id is missing"

    def test_create_user_controller_missing_soc(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo=repo)
        controller = MeasureBatteryController(usecase=usecase)

        request = HttpRequest(body={
            'battery_id': "1",
            # 'soc': 0.5,
            'voltage': 3.7,
            'current': 0.1,
            'temperature': 25.0,
            'timestamp': int(datetime.datetime.now().timestamp())*1000
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field soc is missing"

    def test_create_user_controller_missing_voltage(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo=repo)
        controller = MeasureBatteryController(usecase=usecase)

        request = HttpRequest(body={
            'battery_id': "1",
            'soc': 0.5,
            # 'voltage': 3.7,
            'current': 0.1,
            'temperature': 25.0,
            'timestamp': int(datetime.datetime.now().timestamp())*1000
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field voltage is missing"

    def test_create_user_controller_missing_current(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo=repo)
        controller = MeasureBatteryController(usecase=usecase)

        request = HttpRequest(body={
            'battery_id': "1",
            'soc': 0.5,
            'voltage': 3.7,
            # 'current': 0.1,
            'temperature': 25.0,
            'timestamp': int(datetime.datetime.now().timestamp())*1000
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field current is missing"

    def test_create_user_controller_missing_temperature(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo=repo)
        controller = MeasureBatteryController(usecase=usecase)

        request = HttpRequest(body={
            'battery_id': "1",
            'soc': 0.5,
            'voltage': 3.7,
            'current': 0.1,
            # 'temperature': 25.0,
            'timestamp': int(datetime.datetime.now().timestamp())*1000
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field temperature is missing"

    def test_create_user_controller_invalid_battery_id(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo=repo)
        controller = MeasureBatteryController(usecase=usecase)

        request = HttpRequest(body={
            'battery_id': 1,
            'soc': 0.5,
            'voltage': 3.7,
            'current': 0.1,
            'temperature': 25.0,
            'timestamp': int(datetime.datetime.now().timestamp())*1000
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field battery_id is not valid"

    def test_create_user_controller_invalid_soc(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo=repo)
        controller = MeasureBatteryController(usecase=usecase)

        request = HttpRequest(body={
            'battery_id': "1",
            'soc': "0.5 V",
            'voltage': 3.7,
            'current': 0.1,
            'temperature': 25.0,
            'timestamp': int(datetime.datetime.now().timestamp())*1000
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field soc is not valid"

    def test_create_user_controller_invalid_voltage(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo=repo)
        controller = MeasureBatteryController(usecase=usecase)

        request = HttpRequest(body={
            'battery_id': "1",
            'soc': 0.5,
            'voltage': "3.7 v",
            'current': 0.1,
            'temperature': 25.0,
            'timestamp': int(datetime.datetime.now().timestamp())*1000
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field voltage is not valid"

    def test_create_user_controller_invalid_current(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo=repo)
        controller = MeasureBatteryController(usecase=usecase)

        request = HttpRequest(body={
            'battery_id': "1",
            'soc': 0.5,
            'voltage': 3.7,
            'current': ["0.1"],
            'temperature': 25.0,
            'timestamp': int(datetime.datetime.now().timestamp())*1000
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field current is not valid"

    def test_create_user_controller_invalid_temperature(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo=repo)
        controller = MeasureBatteryController(usecase=usecase)

        request = HttpRequest(body={
            'battery_id': "1",
            'soc': 0.5,
            'voltage': 3.7,
            'current': 0.1,
            'temperature': "25.0 Celsius"
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field temperature is not valid"
