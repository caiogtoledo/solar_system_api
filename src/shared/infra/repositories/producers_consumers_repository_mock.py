from typing import List

from src.shared.domain.entities.solar_panel import SolarPanel
from src.shared.domain.entities.consumer import Consumer
from src.shared.domain.repositories.producers_consumers_repository_interface import IProducersConsumersRepository


class ProducersConsumersRepositoryMock(IProducersConsumersRepository):
    solar_panel_measurements: List[SolarPanel]
    consumer_measurements: List[Consumer]

    def __init__(self):
        self.solar_panel_measurements = [
            SolarPanel(solar_panel_id="1", instantly=100.0,
                       daily=1000.0, monthly=30000.0, timestamp=1643723400000),
            SolarPanel(solar_panel_id="1", instantly=101.0,
                       daily=1001.0, monthly=30001.0, timestamp=1643723410000),
            SolarPanel(solar_panel_id="2", instantly=102.0,
                       daily=1002.0, monthly=30002.0, timestamp=1643723420000),
        ]
        self.consumer_measurements = [
            Consumer(consumer_id="1", instantly=50.0, daily=500.0,
                     monthly=15000.0, timestamp=1643723400000),
            Consumer(consumer_id="1", instantly=51.0, daily=501.0,
                     monthly=15001.0, timestamp=1643723410000),
            Consumer(consumer_id="1", instantly=52.0, daily=502.0,
                     monthly=15002.0, timestamp=1643723420000),
        ]

    def create_solar_panel_measure(self, measure: SolarPanel) -> None:
        self.solar_panel_measurements.append(measure)

    def create_consumer_measure(self, measure: Consumer) -> None:
        self.consumer_measurements.append(measure)

    def get_last_solar_panel_measure(self, solar_panel_id) -> SolarPanel:
        measurements = []
        for measure in self.solar_panel_measurements:
            if measure.solar_panel_id == solar_panel_id:
                measurements.append(measure)
        if len(measurements) == 0:
            return None
        return measurements[-1]

    def get_last_consumer_measure(self, consumer_id) -> Consumer:
        measurements = []
        for measure in self.consumer_measurements:
            if measure.consumer_id == consumer_id:
                measurements.append(measure)
        if len(measurements) == 0:
            return None
        return self.consumer_measurements[-1]

    def get_all_solar_panel_measurements(self, solar_panel_id) -> List[SolarPanel]:
        measurements = []
        for measure in self.solar_panel_measurements:
            if measure.solar_panel_id == solar_panel_id:
                measurements.append(measure)
        return measurements

    def get_all_consumer_measurements(self, consumer_id) -> List[Consumer]:
        measurements = []
        for measure in self.consumer_measurements:
            if measure.consumer_id == consumer_id:
                measurements.append(measure)
        return measurements
