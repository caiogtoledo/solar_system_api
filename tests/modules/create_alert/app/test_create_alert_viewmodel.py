
import datetime

from src.modules.create_alert.app.create_alert_viewmodel import AlertViewmodel
from src.shared.domain.entities.alert import Alert


class Test_AlertViewModel:

    def test_create_alert_viewmodel(self):
        alert = Alert(
            alert_id="1",
            type="baixa_carga_bateria",
            message="A carga da bateria está abaixo de 20%",
            is_resolved=False,
            timestamp_created_at=int(datetime.datetime.now().timestamp()),
            timestamp_updated_at=None
        )
        viewmodel = AlertViewmodel(
            alert=alert).to_dict()

        expected = {
            'alert_id': "1",
            'type': "baixa_carga_bateria",
            'message': "A carga da bateria está abaixo de 20%",
            'is_resolved': False,
            'timestamp_created_at': int(datetime.datetime.now().timestamp()),
            'timestamp_updated_at': None,
        }

        assert expected == viewmodel
