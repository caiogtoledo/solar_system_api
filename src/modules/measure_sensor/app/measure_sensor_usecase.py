

import datetime
from typing import Optional
from src.shared.domain.entities.measurement import Measurement
from src.shared.domain.repositories.measurements_repository_interface import IMeasurementsRepository
from src.shared.helpers.errors.usecase_errors import CreationError


class MeasureSensorUsecase:
    def __init__(self, repo: IMeasurementsRepository):
        self.repo = repo

    def __call__(self, measurement_id: str, value: float, type: str, unit: str, timestamp: Optional[int]) -> Measurement:
        validate = Measurement.validate_measurement_id(measurement_id)
        if not validate:
            raise CreationError("Invalid measurement id")
        validate = Measurement.validate_value(value)
        if not validate:
            raise CreationError("Invalid value")

        if timestamp is None:
            timestamp = int(datetime.datetime.now().timestamp())*1000

        measure = Measurement(
            measurement_id=measurement_id,
            value=value,
            type=type,
            unit=unit,
            timestamp=timestamp
        )

        try:
            self.repo.create_measure(measure)
        except Exception as e:
            raise CreationError(f"Error creating sensor measure: {e}")

        return measure
