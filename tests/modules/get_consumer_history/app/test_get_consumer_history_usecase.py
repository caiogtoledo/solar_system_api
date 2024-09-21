from typing import List
import pytest


from src.modules.get_consumer_history.app.get_consumer_history_usecase import GetConsumerHistoryUsecase
from src.shared.domain.entities.battery import Battery
from src.shared.domain.entities.consumer import Consumer
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock


class Test_GetBatteryStatusHistoryUsecase:

    def test_get_consumer_history(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetConsumerHistoryUsecase(repo)

        test_id = "1"
        history = usecase(
            consumer_id=test_id,
        )

        assert isinstance(history, List)
        consumer_history = history[0]
        assert isinstance(consumer_history, Consumer)
        assert consumer_history.consumer_id == test_id

    def test_get_consumer_id_none(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetConsumerHistoryUsecase(repo)

        with pytest.raises(NoItemsFound):
            history = usecase(
                consumer_id=None,
            )

    def test_get_consumer_id_not_exists(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = GetConsumerHistoryUsecase(repo)

        with pytest.raises(NoItemsFound):
            history = usecase(
                consumer_id="test_abc",
            )
