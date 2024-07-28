from abc import ABC, abstractmethod
from typing import List

from src.shared.domain.entities.battery import Battery


class IBatteryRepository(ABC):

    @abstractmethod
    def create_measure(self, measure: Battery) -> None:
        pass

    @abstractmethod
    def get_all_battery_measurements(self) -> List[Battery]:
        pass
