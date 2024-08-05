
import datetime

from src.modules.measure_consumer.app.measure_consumer_viewmodel import MeasureConsumerViewmodel
from src.shared.domain.entities.consumer import Consumer


class Test_MeasureConsumerViewModel:

    def test_measure_consumer_viewmodel(self):
        solar_panel_measurement = Consumer(
            consumer_id="1",
            instantly=0.5,
            daily=3.7,
            monthly=317.3,
            timestamp=int(datetime.datetime.now().timestamp()),
        )
        userViewmodel = MeasureConsumerViewmodel(
            solar_panel=solar_panel_measurement).to_dict()

        expected = {
            'consumer_id': "1",
            'instantly': 0.5,
            'daily': 3.7,
            'monthly': 317.3,
            'timestamp': int(datetime.datetime.now().timestamp()),
            'message': "the measure was created successfully"
        }

        assert expected == userViewmodel
