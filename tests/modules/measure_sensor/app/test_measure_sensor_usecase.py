import datetime
import pytest

from src.modules.measure_sensor.app.measure_sensor_usecase import MeasureSensorUsecase
from src.shared.helpers.errors.usecase_errors import CreationError
from src.shared.infra.repositories.measurements_repository_mock import MeasurementsRepositoryMock


class Test_MeasureSensorUsecase:

    def test_create_measurement(self):
        repo = MeasurementsRepositoryMock()
        usecase = MeasureSensorUsecase(repo)

        measurement = usecase(
            measurement_id="2",
            value=0.50,
            type="temperature",
            unit="C",
            timestamp=int(datetime.datetime.now().timestamp()),
        )

        assert repo.measurements[-1] == measurement

    def test_create_measurement_without_timestamp(self):
        repo = MeasurementsRepositoryMock()
        usecase = MeasureSensorUsecase(repo)

        measurement = usecase(
            measurement_id="2",
            value=0.50,
            type="temperature",
            unit="C",
            timestamp=None,
        )

        assert repo.measurements[-1] == measurement

    def test_create_consumer_measure_invalid_measurement_id(self):
        repo = MeasurementsRepositoryMock()
        usecase = MeasureSensorUsecase(repo)

        with pytest.raises(CreationError):
            measurement = usecase(
                measurement_id=2,
                value=2,
                type="temperature",
                unit="C",
                timestamp=None,
            )

    def test_create_consumer_measure_invalid_value(self):
        repo = MeasurementsRepositoryMock()
        usecase = MeasureSensorUsecase(repo)

        with pytest.raises(CreationError):
            measurement = usecase(
                measurement_id="2",
                value="teste",
                type="temperature",
                unit="C",
                timestamp=None,
            )
