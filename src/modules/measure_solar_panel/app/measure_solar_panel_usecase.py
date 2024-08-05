

import datetime
from typing import Optional
from src.shared.domain.entities.solar_panel import SolarPanel

from src.shared.domain.repositories.producers_consumers_repository_interface import IProducersConsumersRepository
from src.shared.helpers.errors.usecase_errors import CreationError
from src.shared.helpers.functions.calculate_energy_accumulated import calculate_energy_accumulated


class MeasureSolarPanelUsecase:
    def __init__(self, repo: IProducersConsumersRepository):
        self.repo = repo

    def __call__(self, solar_panel_id: float, instantly: float, timestamp: Optional[int]) -> SolarPanel:
        validate = SolarPanel.validate_solar_panel_id(solar_panel_id)
        if not validate:
            raise CreationError("Invalid solar panel id")
        validate = SolarPanel.validate_instantly(instantly)
        if not validate:
            raise CreationError("Invalid instantly value")

        last_measure: SolarPanel = self.repo.get_last_solar_panel_measure(
            solar_panel_id)

        if timestamp is None:
            timestamp = int(datetime.datetime.now().timestamp())

        if last_measure:
            prev_timestamp = last_measure.timestamp
            daily_accumulated_energy = calculate_energy_accumulated(
                last_measure.daily,
                instantly,
                prev_timestamp,
                timestamp
            )
            monthly_accumulated_energy = calculate_energy_accumulated(
                last_measure.monthly,
                instantly,
                prev_timestamp,
                timestamp)

        # Verificar se o dia ou mês mudou para resetar os acumulados
        if datetime.datetime.fromtimestamp(timestamp).date() != datetime.datetime.fromtimestamp(prev_timestamp).date():
            daily_accumulated_energy = instantly * ((datetime.datetime.fromtimestamp(timestamp) - datetime.datetime.fromtimestamp(
                timestamp).replace(hour=0, minute=0, second=0)).total_seconds() / 3600.0)
        if datetime.datetime.fromtimestamp(timestamp).month != datetime.datetime.fromtimestamp(prev_timestamp).month:
            monthly_accumulated_energy = instantly * ((datetime.datetime.fromtimestamp(timestamp) - datetime.datetime.fromtimestamp(
                timestamp).replace(day=1, hour=0, minute=0, second=0)).total_seconds() / 3600.0)
        else:
            daily_accumulated_energy = instantly
            monthly_accumulated_energy = instantly

        measure = SolarPanel(
            solar_panel_id=solar_panel_id,
            instantly=instantly,
            daily=daily_accumulated_energy,
            monthly=monthly_accumulated_energy,
            timestamp=timestamp
        )

        try:
            self.repo.create_solar_panel_measure(measure)
        except Exception as e:
            raise CreationError(f"Error creating solar panel measure: {e}")

        return measure
