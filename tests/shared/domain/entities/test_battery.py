import pytest
from src.shared.domain.entities.battery import Battery
from src.shared.helpers.errors.domain_errors import EntityError
import datetime


class Test_Battery:
    def test_battery(self):
        measure = Battery(
            battery_id="1",
            soc=0.5,
            voltage=3.7,
            current=0.1,
            temperature=25.0,
            timestamp=int(datetime.datetime.now().timestamp()),
        )

        assert type(measure) == Battery
        assert measure.battery_id == "1"
        assert measure.soc == 0.5
        assert measure.voltage == 3.7
        assert measure.current == 0.1
        assert measure.temperature == 25.0
        assert measure.timestamp == int(datetime.datetime.now().timestamp())

    def test_battery_id_is_none(self):
        with pytest.raises(EntityError):
            measure = Battery(
                battery_id=None,
                soc=0.5,
                voltage=3.7,
                current=0.1,
                temperature=25.0,
                timestamp=int(datetime.datetime.now().timestamp()),
            )

    def test_battery_id_is_not_str(self):
        with pytest.raises(EntityError):
            measure = Battery(
                battery_id=2,
                soc=0.5,
                voltage=3.7,
                current=0.1,
                temperature=25.0,
                timestamp=int(datetime.datetime.now().timestamp()),
            )

    def test_battery_soc_is_none(self):
        with pytest.raises(EntityError):
            measure = Battery(
                battery_id=2,
                soc=None,
                voltage=3.7,
                current=0.1,
                temperature=25.0,
                timestamp=int(datetime.datetime.now().timestamp()),
            )

    def test_battery_soc_is_not_valid(self):
        with pytest.raises(EntityError):
            measure = Battery(
                battery_id=2,
                soc="TESTE",
                voltage=3.7,
                current=0.1,
                temperature=25.0,
                timestamp=int(datetime.datetime.now().timestamp()),
            )

    def test_battery_voltage_is_not_valid(self):
        with pytest.raises(EntityError):
            measure = Battery(
                battery_id=2,
                soc=0.1,
                voltage="TESTE",
                current=0.1,
                temperature=25.0,
                timestamp=int(datetime.datetime.now().timestamp()),
            )

    def test_battery_current_is_not_valid(self):
        with pytest.raises(EntityError):
            measure = Battery(
                battery_id=2,
                soc=0.1,
                voltage=2,
                current="TESTE",
                temperature=25.0,
                timestamp=int(datetime.datetime.now().timestamp()),
            )

    def test_battery_temperature_is_not_valid(self):
        with pytest.raises(EntityError):
            measure = Battery(
                battery_id=2,
                soc=0.1,
                voltage=2,
                current=0.1,
                temperature="TESTE",
                timestamp=int(datetime.datetime.now().timestamp())
            )
# TODO: Implementar teste para o MIN e MAX do Soc
