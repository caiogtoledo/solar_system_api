
import datetime

from src.modules.measure_consumer.app.measure_consumer_viewmodel import MeasureConsumerViewmodel
from src.modules.measure_sensor.app.measure_sensor_viewmodel import MeasureSensorViewmodel
from src.shared.domain.entities.measurement import Measurement


class Test_MeasureSensorViewModel:

    def test_measure_consumer_viewmodel(self):
        measurement = Measurement(
            measurement_id="1",
            value=0.5,
            type="irradiacao_solar",
            unit="W/m2",
            timestamp=int(datetime.datetime.now().timestamp())*1000,
        )
        measurementViewmodel = MeasureSensorViewmodel(
            measure=measurement).to_dict()

        expected = {
            'measurement_id': "1",
            'value': 0.5,
            'type': "irradiacao_solar",
            'unit': "W/m2",
            'timestamp': int(datetime.datetime.now().timestamp())*1000,
            'message': "the measure was created successfully"
        }

        assert expected == measurementViewmodel
