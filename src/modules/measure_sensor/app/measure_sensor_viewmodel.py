from src.shared.domain.entities.measurement import Measurement
from src.shared.domain.enums.state_enum import STATE


class MeasureSensorViewmodel:
    measurement_id: str
    value: float
    type: str
    unit: str
    timestamp: int

    def __init__(self, measure: Measurement):
        self.measurement_id = measure.measurement_id
        self.value = measure.value
        self.type = measure.type
        self.unit = measure.unit
        self.timestamp = measure.timestamp

    def to_dict(self):
        return {
            'measurement_id': self.measurement_id,
            'value': self.value,
            'type': self.type,
            'unit': self.unit,
            'timestamp': self.timestamp,
            'message': "the measure was created successfully"
        }
