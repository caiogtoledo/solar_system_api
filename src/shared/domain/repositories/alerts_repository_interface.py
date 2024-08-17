from abc import ABC, abstractmethod
from typing import List, Optional

from src.shared.domain.entities.battery import Battery


class IAlertsRepository(ABC):

    @abstractmethod
    def create_alert(self, alert: Battery) -> None:
        pass

    @abstractmethod
    def get_all_alerts(self, alert: str) -> List[Battery]:
        pass

    @abstractmethod
    def update_alert(self, alert: str) -> Optional[Battery]:
        pass
