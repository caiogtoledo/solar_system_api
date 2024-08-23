import datetime
import pytest

from src.modules.get_all_alerts.app.get_all_alerts_usecase import GetAllAlertsUsecase
from src.shared.domain.entities.alert import Alert
from src.shared.helpers.errors.usecase_errors import CreationError
from src.shared.infra.repositories.alerts_repository_mock import AlertsRepositoryMock


class Test_GetAllAlertsUsecase:

    def test_get_all_alerts(self):
        repo = AlertsRepositoryMock()
        usecase = GetAllAlertsUsecase(repo)

        alerts = usecase()

        assert all(type(alert) == Alert for alert in alerts)
        assert len(alerts) == len(repo.alerts)
        assert type(repo.alerts) == list
