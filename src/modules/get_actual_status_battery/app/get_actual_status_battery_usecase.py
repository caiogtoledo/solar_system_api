

from typing import Optional
from src.shared.domain.entities.battery import Battery

from src.shared.domain.repositories.battery_repository_interface import IBatteryRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetActualStatusBatteryUsecase:
    def __init__(self, repo: IBatteryRepository):
        self.repo = repo

    def __call__(self, battery_id: float) -> Battery:
        validate = Battery.validate_battery_id(battery_id)
        if not validate:
            raise NoItemsFound("Invalid battery id")

        last_measure: Optional[Battery] = self.repo.get_last_battery_measurement_by_id(
            battery_id)

        if last_measure is None:
            raise NoItemsFound(": battery status")

        return last_measure
