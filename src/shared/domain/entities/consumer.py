import abc

from src.shared.helpers.errors.domain_errors import EntityError


class Consumer(abc.ABC):
    consumer_id: str
    instantly: float # W
    daily: float # KWh
    monthly: float # KWh

    def __init__(self, consumer_id: str, instantly: float, daily: float, monthly: float, temperature: float):
        if not self.validate_consumer_id(consumer_id):
            raise EntityError("consumer_id")
        self.consumer_id = consumer_id

        if not self.validate_instantly(instantly):
            raise EntityError("instantly")
        self.instantly = instantly

        if not self.validate_daily(daily):
            raise EntityError("daily")
        self.daily = daily

        if not self.validate_monthly(monthly):
            raise EntityError("monthly")
        self.monthly = monthly

    @staticmethod
    def validate_consumer_id(consumer_id: str) -> bool:
        return isinstance(consumer_id, str) and len(consumer_id) > 0

    @staticmethod
    def validate_instantly(daily: float) -> bool:
        return isinstance(daily, (int, float))

    @staticmethod
    def validate_daily(daily: float) -> bool:
        return isinstance(daily, (int, float))

    @staticmethod
    def validate_monthly(monthly: float) -> bool:
        return isinstance(monthly, (int, float))


    def __repr__(self):
        return (f"Consumer(consumer_id={self.consumer_id}, instantly={self.instantly}, "
                f"daily={self.daily}, monthly={self.monthly}, "
        )