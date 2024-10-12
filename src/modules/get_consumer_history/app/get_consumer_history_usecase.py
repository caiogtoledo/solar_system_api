

from typing import List, Optional
from src.shared.domain.entities.battery import Battery

from src.shared.domain.entities.consumer import Consumer
from src.shared.domain.repositories.producers_consumers_repository_interface import IProducersConsumersRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetConsumerHistoryUsecase:
    def __init__(self, repo: IProducersConsumersRepository):
        self.repo = repo

    def __call__(self, consumer_id: float) -> List[Consumer]:
        validate = Consumer.validate_consumer_id(consumer_id)
        if not validate:
            raise NoItemsFound("Invalid consumer id")

        history: Optional[List[Consumer]] = self.repo.get_consumer_measurements(
            consumer_id)

        if history is None or len(history) == 0:
            raise NoItemsFound(": consumer history")

        return history
