
import datetime

from src.modules.get_actual_status_battery.app.get_actual_status_battery_viewmodel import GetActualStatusBatteryViewmodel
from src.shared.domain.entities.battery import Battery


class Test_GetActualStatusBatteryViewModel:

    def test_get_solar_panel_production_viewmodel(self):
        test_id = "1"
        measurement = Battery(
            battery_id=test_id,
            soc=0.5,
            voltage=3.7,
            current=317.3,
            temperature=30.3,
            timestamp=int(datetime.datetime.now().timestamp()),
        )
        userViewmodel = GetActualStatusBatteryViewmodel(
            battery=measurement).to_dict()

        expected = {
            'battery_id': test_id,
            'soc': 0.5,
            'voltage': 3.7,
            'current': 317.3,
            'temperature': 30.3,
            'timestamp': int(datetime.datetime.now().timestamp()),
            'message': f"this is the last status of battery: {test_id}"
        }

        assert expected == userViewmodel
