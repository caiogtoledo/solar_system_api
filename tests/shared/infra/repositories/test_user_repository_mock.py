from src.shared.domain.entities.battery import Battery
from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock
import pytest
import datetime


class Test_BatteryRepositoryMock:
    def test_create_measure(self):
        repo = BatteryRepositoryMock()
        measurement = Battery(battery_id="1",
                              soc=0.50,
                              voltage=0.5,
                              current=0.5,
                              temperature=30.0,
                              timestamp=int(
                                  datetime.datetime.now().timestamp())
                              )

        repo.create_measure(measurement)

        assert repo.battery_measurements[-1].battery_id == "1"
        assert repo.battery_measurements[-1].soc == 0.50
        assert repo.battery_measurements[-1].voltage == 0.5
        assert repo.battery_measurements[-1].current == 0.5
        assert repo.battery_measurements[-1].temperature == 30.0
        assert repo.battery_measurements[-1].timestamp == int(
            datetime.datetime.now().timestamp())

    def test_get_all_battery_measurements(self):
        repo = BatteryRepositoryMock()
        battery_measurements = repo.get_all_battery_measurements()
        assert len(battery_measurements) == 3
