import datetime
import pytest


from src.modules.get_actual_status_battery.app.get_actual_status_battery_usecase import GetActualStatusBatteryUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock


class Test_GetActualStatusBatteryUsecase:

    def test_get_actual_status_battery(self):
        repo = BatteryRepositoryMock()
        usecase = GetActualStatusBatteryUsecase(repo)

        actual_status = usecase(
            battery_id="1",
        )

        assert repo.battery_measurements[-1] == actual_status

    def test_get_actual_status_battery_id_none(self):
        repo = BatteryRepositoryMock()
        usecase = GetActualStatusBatteryUsecase(repo)

        with pytest.raises(NoItemsFound):
            actual_status = usecase(
                battery_id=None,
            )

    def test_get_actual_status_battery_id_not_exists(self):
        repo = BatteryRepositoryMock()
        usecase = GetActualStatusBatteryUsecase(repo)

        with pytest.raises(NoItemsFound):
            actual_status = usecase(
                battery_id="test_abc",
            )
