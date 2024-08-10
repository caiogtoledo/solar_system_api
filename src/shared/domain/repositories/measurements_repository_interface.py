from abc import ABC, abstractmethod
from typing import List, Optional

from src.shared.domain.entities.measurement import Measurement


class IMeasurementsRepository(ABC):

    @abstractmethod
    def create_measure(self, measure: Measurement) -> None:
        pass

    @ abstractmethod
    def get_last_measure(self) -> Optional[Measurement]:
        pass
