from src.shared.domain.entities.battery import Battery


class GetActualStatusBatteryViewmodel:
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
            'message': f"this is the last status of battery: {self.battery_id}"
        }
