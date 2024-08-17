
import datetime

from src.modules.get_actual_status_battery.app.get_actual_status_battery_viewmodel import GetActualStatusBatteryViewmodel
from src.modules.get_status_battery_history.app.get_battery_status_history_viewmodel import GetBatteryStatusHistoryViewmodel, StatusBatteryViewmodel
from src.shared.domain.entities.battery import Battery


class Test_GetBatteryStatusHistoryViewModel:

    def test_get_battery_status_viewmodel(self):
        test_id = "1"
        measurement = Battery(
            battery_id=test_id,
            soc=0.5,
            voltage=3.7,
            current=317.3,
            temperature=30.3,
            timestamp=int(datetime.datetime.now().timestamp()),
        )
        viewmodel = StatusBatteryViewmodel(
            battery=measurement).to_dict()

        expected = {
            'battery_id': test_id,
            'soc': 0.5,
            'voltage': 3.7,
            'current': 317.3,
            'temperature': 30.3,
            'timestamp': int(datetime.datetime.now().timestamp()),
        }

        assert expected == viewmodel

    def test_get_battery_status_history_viewmodel(self):
        test_id = "1"
        measurement = Battery(
            battery_id=test_id,
            soc=0.5,
            voltage=3.7,
            current=317.3,
            temperature=30.3,
            timestamp=int(datetime.datetime.now().timestamp()),
        )
        viewmodel = GetBatteryStatusHistoryViewmodel(
            [measurement]).to_dict()

        expected = {
            "battery_status_history": [{
                'battery_id': test_id,
                'soc': 0.5,
                'voltage': 3.7,
                'current': 317.3,
                'temperature': 30.3,
                'timestamp': int(datetime.datetime.now().timestamp()),
            }],
            "message": "Status battery history"
        }

        assert expected == viewmodel
