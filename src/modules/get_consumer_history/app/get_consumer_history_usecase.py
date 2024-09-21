

from typing import Optional
from src.shared.domain.entities.battery import Battery

from src.shared.domain.entities.consumer import Consumer
from src.shared.domain.repositories.producers_consumers_repository_interface import IProducersConsumersRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetConsumerHistoryUsecase:
    def __init__(self, repo: IProducersConsumersRepository):
        self.repo = repo

    def __call__(self, consumer_id: float) -> Battery:
        validate = Consumer.validate_consumer_id(consumer_id)
        if not validate:
            raise NoItemsFound("Invalid consumer id")

        last_measure: Optional[Battery] = self.repo.get(
            consumer_id)

        if last_measure is None:
            raise NoItemsFound(": consumer status")

        return last_measure
