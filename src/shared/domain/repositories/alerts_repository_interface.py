from abc import ABC, abstractmethod
from typing import List

from src.shared.domain.entities.alert import Alert


class IAlertsRepository(ABC):

    @abstractmethod
    def create_alert(self, alert: Alert) -> None:
        pass

    @abstractmethod
    def get_all_alerts(self) -> List[Alert]:
        pass

    @abstractmethod
    def update_alert(self, alert: str) -> Alert:
        pass
