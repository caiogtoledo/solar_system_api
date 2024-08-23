import datetime

from src.modules.get_all_alerts.app.get_all_alerts_controller import GetAllAlertsController
from src.modules.get_all_alerts.app.get_all_alerts_usecase import GetAllAlertsUsecase
from src.shared.domain.entities.alert import Alert
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.alerts_repository_mock import AlertsRepositoryMock


class Test_GetAllAlertsController:

    def test_get_all_alerts_controller(self):
        repo = AlertsRepositoryMock()
        usecase = GetAllAlertsUsecase(repo=repo)
        controller = GetAllAlertsController(usecase=usecase)

        request = HttpRequest(body={})

        response = controller(request=request)

        assert response.status_code == 200
        assert type(response.body['alerts']) == list
        assert len(response.body['alerts']) == len(repo.alerts)
