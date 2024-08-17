from src.shared.domain.entities.alert import Alert


class AlertViewmodel:
    alert_id: str
    type: str
    message: str
    is_resolved: bool
    timestamp: int

    def __init__(self, alert: Alert):
        self.alertment_id = alert.alert_id
        self.type = alert.type
        self.message = alert.message
        self.timestamp = alert.timestamp

    def to_dict(self):
        return {
            'alert_id': self.alert_id,
            'type': self.type,
            'message': self.message,
            'is_resolved': self.is_resolved,
            'timestamp': self.timestamp,
        }
