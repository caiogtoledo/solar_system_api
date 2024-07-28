from typing import List

from src.shared.domain.entities.battery import Battery
from src.shared.domain.repositories.battery_repository_interface import IBatteryRepository


class BatteryRepositoryMock(IBatteryRepository):
    battery_measurements: List[Battery]

    def __init__(self):
        self.battery_measurements = [
            Battery(battery_id="1", soc=0.50, voltage=0.5, current=0.5, temperature=30.0),
            Battery(battery_id="1", soc=0.51, voltage=0.5, current=0.5, temperature=30.1),
            Battery(battery_id="1", soc=0.52, voltage=0.5, current=0.5, temperature=30.2),
        ]
        self.user_counter = 3

    def create_measure(self, new_measurement: Battery) -> Battery:
        self.battery_measurements.append(new_measurement)
        return new_measurement

    def get_all_battery_measurements(self) -> List[Battery]:
        return self.battery_measurements