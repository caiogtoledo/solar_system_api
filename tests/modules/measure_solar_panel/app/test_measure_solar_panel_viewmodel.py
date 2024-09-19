
import datetime
from src.modules.measure_solar_panel.app.measure_solar_panel_viewmodel import MeasureSolarPanelViewmodel
from src.shared.domain.entities.solar_panel import SolarPanel


class Test_MeasureSolarPanelViewModel:

    def test_measure_solar_panel_viewmodel(self):
        solar_panel_measurement = SolarPanel(
            solar_panel_id="1",
            instantly=0.5,
            daily=3.7,
            monthly=317.3,
            timestamp=int(datetime.datetime.now().timestamp())*1000,
        )
        userViewmodel = MeasureSolarPanelViewmodel(
            solar_panel=solar_panel_measurement).to_dict()

        expected = {
            'solar_panel_id': "1",
            'instantly': 0.5,
            'daily': 3.7,
            'monthly': 317.3,
            'timestamp': int(datetime.datetime.now().timestamp())*1000,
            'message': "the measure was created successfully"
        }

        assert expected == userViewmodel
