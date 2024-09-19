import datetime
from src.modules.measure_solar_panel.app.measure_solar_panel_controller import MeasureSolarPanelController
from src.modules.measure_solar_panel.app.measure_solar_panel_usecase import MeasureSolarPanelUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock


class Test_MeasureSolarPanelControler:
    def test_measurement_solar_panel_controller(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureSolarPanelUsecase(repo=repo)
        controller = MeasureSolarPanelController(usecase=usecase)

        request = HttpRequest(body={
            'solar_panel_id': '1',
            'instantly': 0.5,
            'timestamp': int(datetime.datetime.now().timestamp())*1000,
        })

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['solar_panel_id'] == repo.solar_panel_measurements[-1].solar_panel_id
        assert response.body['instantly'] == repo.solar_panel_measurements[-1].instantly
        assert response.body['timestamp'] == repo.solar_panel_measurements[-1].timestamp
        assert isinstance(response.body['timestamp'], int)
        assert response.body['timestamp'] == int(
            datetime.datetime.now().timestamp())*1000
        assert isinstance(response.body['daily'], float)
        assert isinstance(response.body['monthly'], float)
        assert response.body['daily'] <= response.body['monthly']
        assert response.body['message'] == "the measure was created successfully"

    def test_create_solar_panel_measurement_controller_missing_solar_panel_id(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureSolarPanelUsecase(repo=repo)
        controller = MeasureSolarPanelController(usecase=usecase)

        request = HttpRequest(body={
            # 'solar_panel_id': '1',
            'instantly': 0.5,
            'timestamp': int(datetime.datetime.now().timestamp())*1000,
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field solar_panel_id is missing"

    def test_create_solar_panel_measurement_controller_missing_instantly(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureSolarPanelUsecase(repo=repo)
        controller = MeasureSolarPanelController(usecase=usecase)

        request = HttpRequest(body={
            'solar_panel_id': '1',
            # 'instantly': 0.5,
            'timestamp': int(datetime.datetime.now().timestamp())*1000,
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field instantly is missing"

    def test_create_solar_panel_measurement_controller_missing_timestamp(self):
        # Mesmo faltando timestamp, o caso de uso gerará um timestamp
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureSolarPanelUsecase(repo=repo)
        controller = MeasureSolarPanelController(usecase=usecase)

        request = HttpRequest(body={
            'solar_panel_id': '1',
            'instantly': 0.5,
            # 'timestamp': int(datetime.datetime.now().timestamp())*1000,
        })

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['solar_panel_id'] == repo.solar_panel_measurements[-1].solar_panel_id
        assert response.body['instantly'] == repo.solar_panel_measurements[-1].instantly
        assert isinstance(response.body['timestamp'], int)
        assert response.body['timestamp'] == int(
            datetime.datetime.now().timestamp())*1000
        assert isinstance(response.body['daily'], float)
        assert isinstance(response.body['monthly'], float)
        assert response.body['daily'] <= response.body['monthly']

        assert response.body['message'] == "the measure was created successfully"
