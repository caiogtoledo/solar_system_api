from abc import ABC, abstractmethod
from typing import List, Optional

from src.shared.domain.entities.consumer import Consumer
from src.shared.domain.entities.solar_panel import SolarPanel


class IProducersConsumersRepository(ABC):

    @abstractmethod
    def create_solar_panel_measure(self, measure: SolarPanel) -> None:
        pass

    @ abstractmethod
    def create_consumer_measure(self, measure: Consumer) -> None:
        pass

    @ abstractmethod
    def get_last_solar_panel_measure(self, solar_panel_id: str) -> Optional[SolarPanel]:
        pass

    @ abstractmethod
    def get_last_consumer_measure(self, consumer_id: str) -> Optional[Consumer]:
        pass

    @ abstractmethod
    def get_solar_panel_measurements(self, solar_panel_id: str) -> Optional[List[Consumer]]:
        pass

    @ abstractmethod
    def get_all_solar_panels_measurements(self, records: Optional[int]) -> Optional[List[Consumer]]:
        pass

    @ abstractmethod
    def get_consumer_measurements(self, consumer_id: str) -> Optional[List[Consumer]]:
        pass

    @ abstractmethod
    def get_all_consumers_measurements(self, records: Optional[int]) -> Optional[List[Consumer]]:
        pass
