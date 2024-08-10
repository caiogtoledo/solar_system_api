from typing import List

from src.shared.domain.entities.measurement import Measurement
from src.shared.domain.repositories.measurements_repository_interface import IMeasurementsRepository


class MeasurementsRepositoryMock(IMeasurementsRepository):
    measurements: List[Measurement]

    def __init__(self):
        self.measurements = [
            Measurement(measurement_id="1", value=100.0,
                        type="irradiacao_solar", unit="W/m2", timestamp=1643723400),
            Measurement(measurement_id="1", value=101.0,
                        type="irradiacao_solar", unit="W/m2", timestamp=1643723410),
            Measurement(measurement_id="2", value=102.0,
                        type="irradiacao_solar", unit="W/m2", timestamp=1643723420),
        ]

    def create_measure(self, measure: Measurement) -> None:
        self.measurements.append(measure)

    def get_last_measure(self) -> Measurement:
        return self.measurements[-1]
