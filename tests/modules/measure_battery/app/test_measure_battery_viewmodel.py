from src.modules.measure_battery.app.measure_battery_viewmodel import MeasureBatteryViewmodel
from src.shared.domain.entities.battery import Battery
import datetime


class Test_MeasureBatteryViewModel:

    def test_measure_battery_viewmodel(self):
        battery_measurement = Battery(
            battery_id="1",
            soc=0.5,
            voltage=3.7,
            current=0.1,
            temperature=25.0,
            timestamp=int(datetime.datetime.now().timestamp())*1000
        )
        userViewmodel = MeasureBatteryViewmodel(
            battery=battery_measurement).to_dict()

        expected = {
            'battery_id': "1",
            'soc': 0.5,
            'voltage': 3.7,
            'current': 0.1,
            'temperature': 25.0,
            'timestamp': int(datetime.datetime.now().timestamp())*1000,
            'message': "the measure was created successfully"
        }

        assert expected == userViewmodel
