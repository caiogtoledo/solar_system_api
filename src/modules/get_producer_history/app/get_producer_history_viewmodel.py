from typing import List
from src.shared.domain.entities.solar_panel import SolarPanel


class ProducerViewmodel:
    producer_id: str
    instantly: float
    daily: float
    monthly: float
    timestamp: int

    def __init__(self, producer: SolarPanel):
        self.producer_id = producer.solar_panel_id
        self.instantly = producer.instantly
        self.daily = producer.daily
        self.monthly = producer.monthly
        self.timestamp = producer.timestamp

    def to_dict(self):
        return {
            'producer_id': self.producer_id,
            'instantly': self.instantly,
            'daily': self.daily,
            'monthly': self.monthly,
            'timestamp': self.timestamp,
        }


class GetProducerHistoryViewmodel:
    producer_history: List[SolarPanel]

    def __init__(self, producer_history: dict):
        self.producer_history = producer_history

    def to_dict(self):
        return {
            "producer_history": [
                ProducerViewmodel(
                    producer=item
                ).to_dict() for item in self.producer_history],
            "message": "producer history"
        }
