

import datetime
from typing import Optional
from src.shared.domain.entities.alert import Alert
from src.shared.domain.entities.measurement import Measurement
from src.shared.domain.repositories.alerts_repository_interface import IAlertsRepository
from src.shared.helpers.errors.usecase_errors import CreationError


class CreateAlertUsecase:
    def __init__(self, repo: IAlertsRepository):
        self.repo = repo

    def __call__(self, alert_id: str, type: float, message: str, is_resolved: bool, timestamp: Optional[int]) -> Measurement:
        validate = Alert.validate_alert_id(alert_id)
        if not validate:
            raise CreationError("Invalid alert id")
        validate = Alert.validate_type(type)
        if not validate:
            raise CreationError("Invalid type")
        validate = Alert.validate_message(message)
        if not validate:
            raise CreationError("Invalid message")

        if timestamp is None:
            timestamp = int(datetime.datetime.now().timestamp())

        alert = Alert(
            alert_id=alert_id,
            type=type,
            message=message,
            is_resolved=is_resolved or False,
            timestamp=timestamp
        )

        try:
            self.repo.create_alert(alert)
        except Exception as e:
            raise CreationError(f"Error creating sensor alert: {e}")

        return alert
