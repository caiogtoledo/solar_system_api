from typing import List
import pytest

from src.modules.get_producer_history.app.get_producer_history_usecase import GetProducerHistoryUsecase
from src.shared.domain.entities.solar_panel import SolarPanel
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock


class Test_GetBatteryStatusHistoryUsecase:

    def test_get_producer_history(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetProducerHistoryUsecase(repo=repo)

        test_id = "1"
        history = usecase(
            producer_id=test_id,
        )

        assert isinstance(history, List)
        producer_history = history[0]
        assert isinstance(producer_history, SolarPanel)
        assert producer_history.solar_panel_id == test_id

    def test_get_producer_id_none(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetProducerHistoryUsecase(repo)

        with pytest.raises(NoItemsFound):
            history = usecase(
                producer_id=None,
            )

    def test_get_producer_id_not_exists(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetProducerHistoryUsecase(repo)

        with pytest.raises(NoItemsFound):
            history = usecase(
                producer_id="test_abc",
            )
