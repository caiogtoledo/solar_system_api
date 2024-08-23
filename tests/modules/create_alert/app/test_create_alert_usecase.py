import datetime
import pytest

from src.modules.create_alert.app.create_alert_usecase import CreateAlertUsecase
from src.shared.helpers.errors.usecase_errors import CreationError
from src.shared.infra.repositories.alerts_repository_mock import AlertsRepositoryMock


class Test_CreateAlertUsecase:

    def test_create_alert(self):
        repo = AlertsRepositoryMock()
        usecase = CreateAlertUsecase(repo)

        alert = usecase(
            alert_id="2",
            type="serverity",
            message="temperature is too high",
            is_resolved=False,
            timestamp_created_at=int(datetime.datetime.now().timestamp()),
        )

        assert repo.alerts[-1] == alert

    def test_create_alert_without_timestamp(self):
        repo = AlertsRepositoryMock()
        usecase = CreateAlertUsecase(repo)

        alert = usecase(
            alert_id="2",
            type="serverity",
            message="temperature is too high",
            is_resolved=False,
            timestamp_created_at=None,
        )

        assert repo.alerts[-1] == alert

    def test_create_alert_invalid_alert_id(self):
        repo = AlertsRepositoryMock()
        usecase = CreateAlertUsecase(repo)

        with pytest.raises(CreationError):
            alert = usecase(
                alert_id=2,
                type=2,
                message="temperature",
                is_resolved=False,
                timestamp_created_at=int(datetime.datetime.now().timestamp()),
            )

    def test_create_alert_invalid_type(self):
        repo = AlertsRepositoryMock()
        usecase = CreateAlertUsecase(repo)

        with pytest.raises(CreationError):
            alert = usecase(
                alert_id="2",
                type=2,
                message="temperature",
                is_resolved=False,
                timestamp_created_at=None,
            )
