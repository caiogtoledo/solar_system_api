import abc

from src.shared.helpers.errors.domain_errors import EntityError


class Measurement(abc.ABC):
    id: str
    value: float # ex: 100
    type: str # ex: irradiacao_solar (CRIAR UM ENUM?)
    unit: str # ex: W/m2 (CRIAR UM ENUM?)
    timestamp: float # ex: 1631533200 milissigundos

    def __init__(self, measurement_id: str, value: float, type: str, unit: str, timestamp: float):
        if not self.validate_measurement_id(measurement_id):
            raise EntityError("measurement_id")
        self.measurement_id = measurement_id

        if not self.validate_value(value):
            raise EntityError("value")
        self.value = value

        if not self.validate_type(type):
            raise EntityError("type")
        self.type = type

        if not self.validate_unit(unit):
            raise EntityError("unit")
        self.unit = unit

        if not self.validate_timestamp(timestamp):
            raise EntityError("timestamp")
        self.timestamp = timestamp

    @staticmethod
    def validate_measurement_id(measurement_id: str) -> bool:
        return isinstance(measurement_id, str) and len(measurement_id) > 0

    @staticmethod
    def validate_value(value: float) -> bool:
        return isinstance(value, (int, float))

    @staticmethod
    def validate_type(type: str) -> bool:
        return isinstance(type, str) and len(type) > 0
    
    @staticmethod
    def validate_unit(unit: str) -> bool:
        return isinstance(unit, str) and len(unit) > 0

    @staticmethod
    def validate_timestamp(timestamp: float) -> bool:
        return isinstance(timestamp, (int, float))


    def __repr__(self):
        return (f"Measurement(measurement_id={self.measurement_id}, value={self.value}, "
                f"type={self.type}, unit={self.unit}, timestamp={self.timestamp})")