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


class GetBatteryPredictionViewmodel:
    battery_prediction: List[Battery]

    def __init__(self, battery_prediction: dict):
        self.battery_prediction = battery_prediction

    def to_dict(self):
        return {
            "battery_prediction": [
                StatusBatteryViewmodel(
                    battery=status
                ).to_dict() for status in self.battery_prediction],
            "message": "Battery prediction"
        }
