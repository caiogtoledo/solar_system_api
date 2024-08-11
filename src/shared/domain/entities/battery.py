import abc

from src.shared.helpers.errors.domain_errors import EntityError


class Battery(abc.ABC):
    battery_id: str
    soc: float
    voltage: float
    current: float
    temperature: float
    MIN_SOC = 0
    MAX_SOC = 100
    timestamp: int  # milisseconds

    def __init__(self, battery_id: str, soc: float, voltage: float, current: float, temperature: float, timestamp: int):
        if not self.validate_battery_id(battery_id):
            raise EntityError("battery_id")
        self.battery_id = battery_id

        if not self.validate_soc(soc):
            raise EntityError("soc")
        self.soc = soc

        if not self.validate_voltage(voltage):
            raise EntityError("voltage")
        self.voltage = voltage

        if not self.validate_current(current):
            raise EntityError("current")
        self.current = current

        if not self.validate_temperature(temperature):
            raise EntityError("temperature")
        self.temperature = temperature

        if not self.validate_timestamp(timestamp):
            raise EntityError("timestamp")
        self.timestamp = timestamp

    @staticmethod
    def validate_battery_id(battery_id: str) -> bool:
        return isinstance(battery_id, str) and len(battery_id) > 0

    @staticmethod
    def validate_soc(soc: float) -> bool:
        return isinstance(soc, (int, float)) and Battery.MIN_SOC <= soc <= Battery.MAX_SOC

    @staticmethod
    def validate_voltage(voltage: float) -> bool:
        return isinstance(voltage, (int, float))

    @staticmethod
    def validate_current(current: float) -> bool:
        return isinstance(current, (int, float))

    @staticmethod
    def validate_temperature(temperature: float) -> bool:
        return isinstance(temperature, (int, float))

    @staticmethod
    def validate_timestamp(timestamp: int) -> bool:
        return isinstance(timestamp, (int))

    def __repr__(self):
        return (f"Battery(battery_id={self.battery_id}, soc={self.soc}, "
                f"voltage={self.voltage}, current={self.current}, "
                f"temperature={self.temperature}, timestamp={self.timestamp})")
