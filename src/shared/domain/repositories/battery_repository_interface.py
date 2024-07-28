from abc import ABC, abstractmethod
from typing import List

from src.shared.domain.entities.battery import Battery


class IBatteryRepository(ABC):

    @abstractmethod
    def create_measure(self, measure: Battery) -> None:
        pass

    @abstractmethod
    def get_all_user(self) -> List[Battery]:
        pass

    @abstractmethod
    def create_user(self, new_user: Battery) -> Battery:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> Battery:
        """
        If user not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def update_user(self, user_id: int, new_name: str) -> Battery:
        """
        If user not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def get_user_counter(self) -> int:
        """
        Returns the number of all users that have ever been created
        """
        pass
