from typing import List
from src.shared.domain.entities.battery_prediction_time import BatteryPredictionTime


class GetBatteryPredictionTimeViewmodel:
    battery_id: str
    days: int
    hours: int
    minute: int
    charging: bool

    def __init__(self, prediction: BatteryPredictionTime):
        self.battery_id = prediction.battery_id
        self.days = prediction.days
        self.hours = prediction.hours
        self.minute = prediction.minute
        self.charging = prediction.charging

    def to_dict(self):
        return {
            'battery_id': self.battery_id,
            'time': f'{self.days} dias, {self.hours} horas e {self.minute} minutos para {"carregamento" if self.charging else "consumo"} total da bateria',
            'charging': self.charging,
        }
