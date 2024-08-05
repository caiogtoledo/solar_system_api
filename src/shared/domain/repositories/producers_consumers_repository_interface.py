from abc import ABC, abstractmethod
from typing import List

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
    def get_last_solar_panel_measure(self, solar_panel_id: str) -> SolarPanel:
        pass

    @ abstractmethod
    def get_last_consumer_measure(self, consumer_id: str) -> Consumer:
        pass
