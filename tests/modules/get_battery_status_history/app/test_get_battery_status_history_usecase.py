from typing import List
import pytest


from src.modules.get_status_battery_history.app.get_battery_status_history_usecase import GetBatteryStatusHistoryUsecase
from src.shared.domain.entities.battery import Battery
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock


class Test_GetBatteryStatusHistoryUsecase:

    def test_get_battery_status_history(self):
        repo = BatteryRepositoryMock()
        usecase = GetBatteryStatusHistoryUsecase(repo)

        test_id = "1"
        history = usecase(
            battery_id=test_id,
        )

        assert isinstance(history, List)
        battery_history = history[0]
        assert isinstance(battery_history, Battery)
        assert battery_history.battery_id == test_id

    def test_get_battery_status_id_none(self):
        repo = BatteryRepositoryMock()
        usecase = GetBatteryStatusHistoryUsecase(repo)

        with pytest.raises(NoItemsFound):
            actual_status = usecase(
                battery_id=None,
            )

    def test_get_battery_status_id_not_exists(self):
        repo = BatteryRepositoryMock()
        usecase = GetBatteryStatusHistoryUsecase(repo)

        with pytest.raises(NoItemsFound):
            actual_status = usecase(
                battery_id="test_abc",
            )
