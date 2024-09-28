
import datetime
from src.modules.get_producer_history.app.get_producer_history_viewmodel import GetProducerHistoryViewmodel, ProducerViewmodel
from src.shared.domain.entities.solar_panel import SolarPanel


class Test_GetProducerHistoryViewModel:

    def test_get_producer_viewmodel(self):
        test_id = "1"
        producer = SolarPanel(
            solar_panel_id=test_id,
            instantly=0.5,
            daily=3.7,
            monthly=317.3,
            timestamp=int(datetime.datetime.now().timestamp()),
        )
        viewmodel = ProducerViewmodel(
            producer=producer).to_dict()

        expected = {
            'producer_id': test_id,
            'instantly': 0.5,
            'daily': 3.7,
            'monthly': 317.3,
            'timestamp': int(datetime.datetime.now().timestamp()),
        }

        assert expected == viewmodel

    def test_get_producer_history_viewmodel(self):
        test_id = "1"
        producer = SolarPanel(
            solar_panel_id=test_id,
            instantly=0.5,
            daily=3.7,
            monthly=317.3,
            timestamp=int(datetime.datetime.now().timestamp()),
        )
        viewmodel = GetProducerHistoryViewmodel(
            [producer]).to_dict()

        expected = {
            "producer_history": [{
                'producer_id': test_id,
                'instantly': 0.5,
                'daily': 3.7,
                'monthly': 317.3,
                'timestamp': int(datetime.datetime.now().timestamp()),
            }],
            "message": "producer history"
        }

        assert expected == viewmodel
