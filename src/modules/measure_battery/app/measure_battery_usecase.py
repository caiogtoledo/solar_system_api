

from src.shared.domain.entities.battery import Battery
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.repositories.battery_repository_interface import IBatteryRepository
from src.shared.helpers.errors.domain_errors import EntityError


class MeasureBatteryUsecase:
    def __init__(self, repo: IBatteryRepository):
        self.repo = repo

    def __call__(self, battery_id: float, soc: float, voltage: float, current: float, temperature: float, timestamp: int) -> Battery:

        measure = Battery(
            battery_id=battery_id,
            soc=soc,
            voltage=voltage,
            current=current,
            temperature=temperature,
            timestamp=timestamp
        )

        return self.repo.create_measure(measure)
