from src.shared.domain.entities.consumer import Consumer
from src.shared.domain.enums.state_enum import STATE


class MeasureConsumerViewmodel:
    consumer_id: str
    instantly: float
    daily: float
    monthly: float
    timestamp: int

    def __init__(self, solar_panel: Consumer):
        self.consumer_id = solar_panel.consumer_id
        self.instantly = solar_panel.instantly
        self.daily = solar_panel.daily
        self.monthly = solar_panel.monthly
        self.timestamp = solar_panel.timestamp

    def to_dict(self):
        return {
            'consumer_id': self.consumer_id,
            'instantly': self.instantly,
            'daily': self.daily,
            'monthly': self.monthly,
            'timestamp': self.timestamp,
            'message': "the measure was created successfully"
        }
