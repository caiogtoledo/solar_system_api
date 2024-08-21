from typing import List

from src.shared.domain.entities.alert import Alert
from src.shared.domain.repositories.alerts_repository_interface import IAlertsRepository


class AlertsRepositoryMock(IAlertsRepository):
    measurements: List[Alert]

    def __init__(self):
        self.alerts = [
            Alert(
                alert_id="1",
                type="irradiacao_solar",
                message="Alerta 1",
                is_resolved=False,
                timestamp_created_at=1643723400,
                timestamp_updated_at=None
            ),
            Alert(
                alert_id="2",
                type="irradiacao_solar",
                message="Alerta 2",
                is_resolved=True,
                timestamp_created_at=1643723410,
                timestamp_updated_at=1643723415
            ),
            Alert(
                alert_id="3",
                type="irradiacao_solar",
                message="Alerta 3",
                is_resolved=False,
                timestamp_created_at=1643723420,
                timestamp_updated_at=None
            ),
        ]

    def create_alert(self, alert: Alert) -> None:
        self.alerts.append(alert)

    def get_all_alerts(self) -> List[Alert]:
        return self.alerts

    def update_alert(self, alert: Alert) -> Alert:
        # update alert and mantain the same alert_id and index
        for i, a in enumerate(self.alerts):
            if a.alert_id == alert.alert_id:
                self.alerts[i] = alert
        return alert
