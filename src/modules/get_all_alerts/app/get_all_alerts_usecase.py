

import datetime
from typing import List, Optional
from src.shared.domain.entities.alert import Alert
from src.shared.domain.repositories.alerts_repository_interface import IAlertsRepository
from src.shared.helpers.errors.usecase_errors import CreationError


class GetAllAlertsUsecase:
    def __init__(self, repo: IAlertsRepository):
        self.repo = repo

    def __call__(self) -> List[Alert]:
        alerts = self.repo.get_all_alerts()
        alerts.sort(key=lambda x: x.timestamp_created_at)

        return alerts
