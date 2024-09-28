import abc
from typing import Optional
import uuid

from src.shared.helpers.errors.domain_errors import EntityError


class Alert(abc.ABC):
    alert_id: str
    type: float  # ex: baixa_carga_bateria
    message: str  #
    is_resolved: bool
    timestamp_created_at: int  # ex: 1631533200 milissigundos
    timestamp_updated_at: Optional[int]  # ex: 1631533200 milissigundos

    def __init__(self,
                 alert_id: str,
                 type: str,
                 message: str,
                 timestamp_created_at: float,
                 timestamp_updated_at: float,
                 is_resolved: bool
                 ):
        if not self.validate_alert_id(alert_id):
            raise EntityError("alert_id")
        self.alert_id = alert_id

        if not self.validate_type(type):
            raise EntityError("type")
        self.type = type

        if not self.validate_message(message):
            raise EntityError("message")
        self.message = message

        if not self.validate_is_resolved(is_resolved):
            raise EntityError("is_resolved")
        self.is_resolved = is_resolved

        if not self.validate_timestamp(timestamp_created_at):
            raise EntityError("timestamp_created_at")
        self.timestamp_created_at = timestamp_created_at

        self.timestamp_updated_at = timestamp_updated_at

    @staticmethod
    def validate_alert_id(alert_id: str) -> bool:
        return isinstance(alert_id, str) and len(alert_id) > 0

    @staticmethod
    def validate_type(type: str) -> bool:
        return isinstance(type, str) and len(type) > 0

    @staticmethod
    def validate_message(message: str) -> bool:
        return isinstance(message, str) and len(message) > 0

    @staticmethod
    def validate_is_resolved(is_resolved: bool) -> bool:
        return isinstance(is_resolved, (bool))

    @staticmethod
    def validate_timestamp(timestamp: float) -> bool:
        return isinstance(timestamp, (int, float))

    @staticmethod
    def validate_uuid(value: float) -> bool:
        try:
            uuid_obj = uuid.UUID(value, version=4)
        except ValueError:
            return False
        return str(uuid_obj) == value

    def __repr__(self):
        return (f"Alert(alert_id={self.alert_id}, type={self.type}, "
                f"message={self.message}, is_resolved={self.is_resolved}, "
                f"timestamp_created_at={self.timestamp_created_at}, "
                f"timestamp_updated_at={self.timestamp_created_at}"
                )
