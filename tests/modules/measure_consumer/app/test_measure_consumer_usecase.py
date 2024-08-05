import datetime
import pytest


from src.modules.measure_consumer.app.measure_consumer_usecase import MeasureConsumerUsecase
from src.shared.helpers.errors.usecase_errors import CreationError
from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock


class Test_MeasureConsumerUsecase:

    def test_create_consumer_measurement(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureConsumerUsecase(repo)

        consumer_measurement = usecase(
            consumer_id="2",
            instantly=0.50,
            timestamp=int(datetime.datetime.now().timestamp()),
        )

        assert repo.consumer_measurements[-1] == consumer_measurement

    def test_create_consumer_measurement_without_timestamp(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureConsumerUsecase(repo)

        consumer_measurement = usecase(
            consumer_id="2",
            instantly=0.50,
            timestamp=None,
        )

        assert repo.consumer_measurements[-1] == consumer_measurement

    def test_create_consumer_measure_invalid_consumer_id(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureConsumerUsecase(repo)

        with pytest.raises(CreationError):
            consumer_measurement = usecase(
                consumer_id=2,
                instantly=2,
                timestamp=None,
            )

    def test_create_consumer_measure_invalid_instantly(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureConsumerUsecase(repo)

        with pytest.raises(CreationError):
            consumer_measurement = usecase(
                consumer_id="2",
                instantly="teste",
                timestamp=None,
            )
