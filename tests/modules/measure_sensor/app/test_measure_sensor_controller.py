import datetime

from src.modules.measure_sensor.app.measure_sensor_controller import MeasureSensorController
from src.modules.measure_sensor.app.measure_sensor_usecase import MeasureSensorUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.measurements_repository_mock import MeasurementsRepositoryMock


class Test_MeasureSensorControler:

    def test_measurement_measure_sensor_controller(self):
        repo = MeasurementsRepositoryMock()
        usecase = MeasureSensorUsecase(repo=repo)
        controller = MeasureSensorController(usecase=usecase)

        request = HttpRequest(body={
            'measurement_id': '1',
            'value': 0.5,
            'type': 'temperature',
            'unit': 'C',
            'timestamp': int(datetime.datetime.now().timestamp()),
        })

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['measurement_id'] == repo.measurements[-1].measurement_id
        assert response.body['value'] == repo.measurements[-1].value
        assert response.body['timestamp'] == repo.measurements[-1].timestamp
        assert isinstance(response.body['timestamp'], int)
        assert response.body['timestamp'] == int(
            datetime.datetime.now().timestamp())
        assert isinstance(response.body['type'], str)
        assert isinstance(response.body['unit'], str)
        assert response.body['message'] == "the measure was created successfully"

    def test_create_sensor_measure_controller_missing_measurement_id(self):
        repo = MeasurementsRepositoryMock()
        usecase = MeasureSensorUsecase(repo=repo)
        controller = MeasureSensorController(usecase=usecase)

        request = HttpRequest(body={
            # 'measurement_id': '1',
            'value': 0.5,
            'type': 'temperature',
            'unit': 'C',
            'timestamp': int(datetime.datetime.now().timestamp()),
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field measurement_id is missing"

    def test_create_sensor_measure_controller_missing_value(self):
        repo = MeasurementsRepositoryMock()
        usecase = MeasureSensorUsecase(repo=repo)
        controller = MeasureSensorController(usecase=usecase)

        request = HttpRequest(body={
            'measurement_id': '1',
            # 'value': 0.5,
            'type': 'temperature',
            'unit': 'C',
            'timestamp': int(datetime.datetime.now().timestamp()),
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field value is missing"

    def test_create_sensor_measure_controller_missing_timestamp(self):
        # Mesmo faltando timestamp, o caso de uso gerará um timestamp
        repo = MeasurementsRepositoryMock()
        usecase = MeasureSensorUsecase(repo=repo)
        controller = MeasureSensorController(usecase=usecase)

        request = HttpRequest(body={
            'measurement_id': '1',
            'value': 0.5,
            'type': 'temperature',
            'unit': 'C',
            # 'timestamp': int(datetime.datetime.now().timestamp()),
        })

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['measurement_id'] == repo.measurements[-1].measurement_id
        assert response.body['value'] == repo.measurements[-1].value
        assert isinstance(response.body['timestamp'], int)
        assert response.body['timestamp'] == int(
            datetime.datetime.now().timestamp())
        assert isinstance(response.body['type'], str)
        assert isinstance(response.body['unit'], str)

        assert response.body['message'] == "the measure was created successfully"
