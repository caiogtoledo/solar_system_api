

import datetime
from typing import Optional
from src.shared.domain.entities.alert import Alert
from src.shared.domain.repositories.alerts_repository_interface import IAlertsRepository
from src.shared.helpers.errors.usecase_errors import CreationError


class CreateAlertUsecase:
    def __init__(self, repo: IAlertsRepository):
        self.repo = repo

    def __call__(self, alert_id: str, type: float, message: str, is_resolved: bool, timestamp_created_at: Optional[int]) -> Alert:
        validate = Alert.validate_alert_id(alert_id)
        if not validate:
            raise CreationError("Invalid alert id")
        validate = Alert.validate_type(type)
        if not validate:
            raise CreationError("Invalid type")
        validate = Alert.validate_message(message)
        if not validate:
            raise CreationError("Invalid message")

        if timestamp_created_at is None:
            timestamp_created_at = int(
                datetime.datetime.now().timestamp())*1000

        alert = Alert(
            alert_id=alert_id,
            type=type,
            message=message,
            is_resolved=is_resolved or False,
            timestamp_created_at=timestamp_created_at,
            timestamp_updated_at=None
        )

        try:
            self.repo.create_alert(alert)
        except Exception as e:
            raise CreationError(f"Error creating sensor alert: {e}")

        return alert
