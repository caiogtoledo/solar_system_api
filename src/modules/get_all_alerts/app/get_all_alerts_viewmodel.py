from typing import Optional
from src.shared.domain.entities.alert import Alert


class AlertViewmodel:
    alert_id: str
    type: str
    message: str
    is_resolved: bool
    timestamp_created_at: int
    timestamp_updated_at: Optional[int]

    def __init__(self, alert: Alert):
        self.alert_id = alert.alert_id
        self.type = alert.type
        self.message = alert.message
        self.is_resolved = alert.is_resolved
        self.timestamp_created_at = alert.timestamp_created_at
        self.timestamp_updated_at = alert.timestamp_updated_at

    def to_dict(self):
        return {
            'alert_id': self.alert_id,
            'type': self.type,
            'message': self.message,
            'is_resolved': self.is_resolved,
            'timestamp_created_at': self.timestamp_created_at,
            'timestamp_updated_at': self.timestamp_updated_at,
        }


class GetAllAlertsViewmodel:
    alerts: list[AlertViewmodel]

    def __init__(self, alerts: list[Alert]):
        self.alerts = [AlertViewmodel(alert).to_dict() for alert in alerts]

    def to_dict(self):
        return {
            'alerts': self.alerts
        }
