from typing import List
from src.shared.domain.entities.consumer import Consumer


class ConsumerViewmodel:
    consumer_id: str
    instantly: float
    daily: float
    monthly: float
    timestamp: int

    def __init__(self, consumer: Consumer):
        self.consumer_id = consumer.consumer_id
        self.instantly = consumer.instantly
        self.daily = consumer.daily
        self.monthly = consumer.monthly
        self.timestamp = consumer.timestamp

    def to_dict(self):
        return {
            'consumer_id': self.consumer_id,
            'instantly': self.instantly,
            'daily': self.daily,
            'monthly': self.monthly,
            'timestamp': self.timestamp,
            'message': "the measure was created successfully"
        }


class GetConsumerHistoryViewmodel:
    consumer_history: List[Consumer]

    def __init__(self, consumer_history: dict):
        self.consumer_history = consumer_history

    def to_dict(self):
        return {
            "consumer_history": [
                ConsumerViewmodel(
                    consumer=item
                ).to_dict() for item in self.consumer_history],
            "message": "Consumer history"
        }
