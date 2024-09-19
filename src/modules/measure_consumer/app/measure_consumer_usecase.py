

import datetime
from typing import Optional
from src.shared.domain.entities.consumer import Consumer
from src.shared.domain.repositories.producers_consumers_repository_interface import IProducersConsumersRepository
from src.shared.helpers.errors.usecase_errors import CreationError
from src.shared.helpers.functions.calculate_energy_accumulated import calculate_energy_accumulated


class MeasureConsumerUsecase:
    def __init__(self, repo: IProducersConsumersRepository):
        self.repo = repo

    def __call__(self, consumer_id: str, instantly: float, timestamp: Optional[int]) -> Consumer:
        validate = Consumer.validate_consumer_id(consumer_id)
        if not validate:
            raise CreationError("Invalid consumer id")
        validate = Consumer.validate_instantly(instantly)
        if not validate:
            raise CreationError("Invalid instantly value")
        last_measure: Optional[Consumer] = self.repo.get_last_consumer_measure(
            consumer_id)

        if timestamp is None:
            timestamp = int(datetime.datetime.now().timestamp())*1000

        if last_measure is not None:
            prev_timestamp = last_measure.timestamp
            daily_accumulated_energy = calculate_energy_accumulated(
                last_measure.daily,
                instantly,
                prev_timestamp/1000,
                timestamp/1000
            )
            monthly_accumulated_energy = calculate_energy_accumulated(
                last_measure.monthly,
                instantly,
                prev_timestamp/1000,
                timestamp/1000)

            # Verificar se o dia ou mês mudou para resetar os acumulados
            if datetime.datetime.fromtimestamp(timestamp/1000).date() != datetime.datetime.fromtimestamp(prev_timestamp/1000).date():
                daily_accumulated_energy = instantly * ((datetime.datetime.fromtimestamp(timestamp/1000) - datetime.datetime.fromtimestamp(
                    timestamp/1000).replace(hour=0, minute=0, second=0)).total_seconds() / 3600.0)
            if datetime.datetime.fromtimestamp(timestamp/1000).month != datetime.datetime.fromtimestamp(prev_timestamp/1000).month:
                monthly_accumulated_energy = instantly * ((datetime.datetime.fromtimestamp(timestamp/1000) - datetime.datetime.fromtimestamp(
                    timestamp/1000).replace(day=1, hour=0, minute=0, second=0)).total_seconds() / 3600.0)
        else:
            daily_accumulated_energy = instantly
            monthly_accumulated_energy = instantly

        measure = Consumer(
            consumer_id=consumer_id,
            instantly=instantly,
            daily=daily_accumulated_energy,
            monthly=monthly_accumulated_energy,
            timestamp=timestamp
        )

        try:
            self.repo.create_consumer_measure(measure)
        except Exception as e:
            raise CreationError(f"Error creating consumer measure: {e}")

        return measure
