from typing import List
from src.shared.domain.entities.battery import Battery


class StatusBatteryViewmodel:
    battery_id: str
    soc: float
    voltage: float
    current: float
    temperature: float
    timestamp: int

    def __init__(self, battery: Battery):
        self.battery_id = battery.battery_id
        self.soc = battery.soc
        self.voltage = battery.voltage
        self.current = battery.current
        self.temperature = battery.temperature
        self.timestamp = battery.timestamp

    def to_dict(self):
        return {
            'battery_id': self.battery_id,
            'soc': self.soc,
            'voltage': self.voltage,
            'current': self.current,
            'temperature': self.temperature,
            'timestamp': self.timestamp,
        }


class GetBatteryStatusHistoryViewmodel:
    status_history: List[Battery]

    def __init__(self, status_history: dict):
        self.status_history = status_history

    def to_dict(self):
        return {
            "battery_status_history": [
                StatusBatteryViewmodel(
                    battery=status
                ).to_dict() for status in self.status_history],
            "message": "Status battery history"
        }
