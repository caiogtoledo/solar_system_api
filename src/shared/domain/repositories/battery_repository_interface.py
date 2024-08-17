from abc import ABC, abstractmethod
from typing import List, Optional

from src.shared.domain.entities.battery import Battery


class IBatteryRepository(ABC):

    @abstractmethod
    def create_measure(self, measure: Battery) -> None:
        pass

    @abstractmethod
    def get_all_battery_measurements(self, battery_id: str) -> List[Battery]:
        pass

    @abstractmethod
    def get_last_battery_measurement_by_id(self, battery_id: str) -> Optional[Battery]:
        pass
