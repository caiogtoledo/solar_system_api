import datetime

from src.modules.get_solar_panel_production.app.get_solar_panel_production_controller import GetSolarPanelProductionController
from src.modules.get_solar_panel_production.app.get_solar_panel_production_usecase import GetSolarPanelProductionUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock


class Test_MeasureSolarPanelControler:
    def test_get_solar_panel_production_controller(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetSolarPanelProductionUsecase(repo=repo)
        controller = GetSolarPanelProductionController(usecase=usecase)

        test_id = "1"

        request = HttpRequest(body={
            'solar_panel_id': '1',
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['solar_panel_id'] == test_id

        assert isinstance(response.body['timestamp'], int)
        assert isinstance(response.body['instantly'], float)
        assert isinstance(response.body['daily'], float)
        assert isinstance(response.body['monthly'], float)

        assert response.body['daily'] <= response.body['monthly']
        assert response.body['message'] == f"this is the last measure of the solar panel: {
            response.body['solar_panel_id']}"

    def test_get_solar_panel_production_controller_missing_solar_panel_id(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetSolarPanelProductionUsecase(repo=repo)
        controller = GetSolarPanelProductionController(usecase=usecase)

        request = HttpRequest(body={
            # 'solar_panel_id': '1',
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field solar_panel_id is missing"

    def test_get_solar_panel_production_controller_invalid_solar_panel_id(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetSolarPanelProductionUsecase(repo=repo)
        controller = GetSolarPanelProductionController(usecase=usecase)

        request = HttpRequest(body={
            'solar_panel_id': 1,
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field solar_panel_id isn't in the right type.\n Received: <class 'int'>.\n Expected: str"

    def test_get_solar_panel_production_controller_not_found(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetSolarPanelProductionUsecase(repo=repo)
        controller = GetSolarPanelProductionController(usecase=usecase)

        request = HttpRequest(body={
            'solar_panel_id': "test_abc",
        })

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == "No items found for : solar panel production energy"
