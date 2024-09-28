

from typing import List, Optional

from src.shared.domain.entities.solar_panel import SolarPanel
from src.shared.domain.repositories.producers_consumers_repository_interface import IProducersConsumersRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetProducerHistoryUsecase:
    def __init__(self, repo: IProducersConsumersRepository):
        self.repo = repo

    def __call__(self, producer_id: float) -> List[SolarPanel]:
        validate = SolarPanel.validate_solar_panel_id(producer_id)
        if not validate:
            raise NoItemsFound("Invalid producer id")

        history: Optional[List[SolarPanel]] = self.repo.get_all_solar_panel_measurements(
            producer_id)

        if history is None or len(history) == 0:
            raise NoItemsFound(": producer history")

        return history
