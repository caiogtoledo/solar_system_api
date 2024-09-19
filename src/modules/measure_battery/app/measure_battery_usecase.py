

from typing import Optional
import datetime
from src.shared.domain.entities.battery import Battery
from src.shared.domain.repositories.battery_repository_interface import IBatteryRepository
from src.shared.helpers.errors.usecase_errors import CreationError


class MeasureBatteryUsecase:
    def __init__(self, repo: IBatteryRepository):
        self.repo = repo

    def __call__(self, battery_id: float, soc: float, voltage: float, current: float, temperature: float, timestamp: Optional[int]) -> Battery:

        if timestamp is None:
            timestamp = int(datetime.datetime.now().timestamp())*1000

        measure = Battery(
            battery_id=battery_id,
            soc=soc,
            voltage=voltage,
            current=current,
            temperature=temperature,
            timestamp=timestamp
        )

        try:
            self.repo.create_measure(measure)
        except Exception as e:
            raise CreationError("Error creating battery measure: {e}")

        return measure
