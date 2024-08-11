import datetime
import pytest


from src.modules.get_solar_panel_production.app.get_solar_panel_production_usecase import GetSolarPanelProductionUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock


class Test_GetSolarPanelProductionUsecase:

    def test_get_solar_panel_production(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetSolarPanelProductionUsecase(repo)

        solar_panel_measurement = usecase(
            solar_panel_id="1",
        )

        assert repo.solar_panel_measurements[1] == solar_panel_measurement

    def test_create_solar_panel_measurement_solar_panel_id_none(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetSolarPanelProductionUsecase(repo)

        with pytest.raises(NoItemsFound):
            solar_panel_measurement = usecase(
                solar_panel_id=None,
            )

    def test_create_solar_panel_measurement_solar_panel_id_not_exists(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetSolarPanelProductionUsecase(repo)

        with pytest.raises(NoItemsFound):
            solar_panel_measurement = usecase(
                solar_panel_id="test_abc",
            )
