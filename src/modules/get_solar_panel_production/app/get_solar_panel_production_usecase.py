

from typing import Optional
from src.shared.domain.entities.solar_panel import SolarPanel

from src.shared.domain.repositories.producers_consumers_repository_interface import IProducersConsumersRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetSolarPanelProductionUsecase:
    def __init__(self, repo: IProducersConsumersRepository):
        self.repo = repo

    def __call__(self, solar_panel_id: float) -> SolarPanel:
        validate = SolarPanel.validate_solar_panel_id(solar_panel_id)
        if not validate:
            raise NoItemsFound("Invalid solar panel id")

        last_measure: Optional[SolarPanel] = self.repo.get_last_solar_panel_measure(
            solar_panel_id)

        if last_measure is None:
            raise NoItemsFound(": solar panel production energy")

        return last_measure
