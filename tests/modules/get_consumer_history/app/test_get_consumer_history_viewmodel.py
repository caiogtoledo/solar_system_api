
import datetime

from src.modules.get_consumer_history.app.get_consumer_history_viewmodel import ConsumerViewmodel, GetConsumerHistoryViewmodel
from src.modules.get_status_battery_history.app.get_battery_status_history_viewmodel import GetBatteryStatusHistoryViewmodel, StatusBatteryViewmodel
from src.shared.domain.entities.battery import Battery
from src.shared.domain.entities.consumer import Consumer


class Test_GetConsumerHistoryViewModel:

    def test_get_consumer_viewmodel(self):
        test_id = "1"
        consumer = Consumer(
            consumer_id=test_id,
            instantly=0.5,
            daily=3.7,
            monthly=317.3,
            timestamp=int(datetime.datetime.now().timestamp()),
        )
        viewmodel = ConsumerViewmodel(
            consumer=consumer).to_dict()

        expected = {
            'consumer_id': test_id,
            'instantly': 0.5,
            'daily': 3.7,
            'monthly': 317.3,
            'timestamp': int(datetime.datetime.now().timestamp()),
        }

        assert expected == viewmodel

    def test_get_battery_status_history_viewmodel(self):
        test_id = "1"
        consumer = Consumer(
            consumer_id=test_id,
            instantly=0.5,
            daily=3.7,
            monthly=317.3,
            timestamp=int(datetime.datetime.now().timestamp()),
        )
        viewmodel = GetConsumerHistoryViewmodel(
            [consumer]).to_dict()

        expected = {
            "consumer_history": [{
                'consumer_id': test_id,
                'instantly': 0.5,
                'daily': 3.7,
                'monthly': 317.3,
                'timestamp': int(datetime.datetime.now().timestamp()),
            }],
            "message": "Consumer history"
        }

        assert expected == viewmodel
