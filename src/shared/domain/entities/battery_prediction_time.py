import abc

from src.shared.helpers.errors.domain_errors import EntityError


class BatteryPredictionTime(abc.ABC):
    battery_id: str
    days: int
    hours: int
    minute: int
    charging: bool

    def __init__(self, battery_id: str, days: int, hours: int, minutes: int, charging: bool):
        if not self.validate_battery_id(battery_id):
            raise EntityError("battery_id")
        self.battery_id = battery_id
        self.days = days
        self.hours = hours
        self.minute = minutes
        self.charging = charging

    @staticmethod
    def validate_battery_id(battery_id: str) -> bool:
        return isinstance(battery_id, str) and len(battery_id) > 0

    def __repr__(self):
        return (f"Battery(battery_id={self.battery_id}, days={self.days}, "
                f"hours={self.hours}, minute={self.current}, "
                f"charging={self.charging})")
