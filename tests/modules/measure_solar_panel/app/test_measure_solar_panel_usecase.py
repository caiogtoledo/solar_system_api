import datetime
import pytest


from src.modules.measure_solar_panel.app.measure_solar_panel_usecase import MeasureSolarPanelUsecase
from src.shared.helpers.errors.usecase_errors import CreationError
from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock
from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock


class Test_MeasureSolarPanelUsecase:

    def test_create_solar_panel_measurement(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureSolarPanelUsecase(repo)

        solar_panel_measurement = usecase(
            solar_panel_id="2",
            instantly=0.50,
            timestamp=int(datetime.datetime.now().timestamp())*1000,
        )

        assert repo.solar_panel_measurements[-1] == solar_panel_measurement

    def test_create_solar_panel_measurement_without_timestamp(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureSolarPanelUsecase(repo)

        solar_panel_measurement = usecase(
            solar_panel_id="2",
            instantly=0.50,
            timestamp=None,
        )

        assert repo.solar_panel_measurements[-1] == solar_panel_measurement

    def test_create_solar_panel_measurement_invalid_solar_panel_id(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureSolarPanelUsecase(repo)

        with pytest.raises(CreationError):
            solar_panel_measurement = usecase(
                solar_panel_id=2,
                instantly=2,
                timestamp=None,
            )

    def test_create_solar_panel_measurement_invalid_instantly(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureSolarPanelUsecase(repo)

        with pytest.raises(CreationError):
            solar_panel_measurement = usecase(
                solar_panel_id="2",
                instantly="teste",
                timestamp=None,
            )
