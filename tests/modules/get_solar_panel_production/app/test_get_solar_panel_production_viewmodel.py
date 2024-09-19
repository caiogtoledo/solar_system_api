
import datetime
from src.modules.get_solar_panel_production.app.get_solar_panel_production_viewmodel import GetSolarPanelProductionViewmodel
from src.shared.domain.entities.solar_panel import SolarPanel


class Test_GetSolarPanelProductionViewModel:

    def test_get_solar_panel_production_viewmodel(self):
        test_id = "1"
        solar_panel_measurement = SolarPanel(
            solar_panel_id=test_id,
            instantly=0.5,
            daily=3.7,
            monthly=317.3,
            timestamp=int(datetime.datetime.now().timestamp())*1000,
        )
        userViewmodel = GetSolarPanelProductionViewmodel(
            solar_panel=solar_panel_measurement).to_dict()

        expected = {
            'solar_panel_id': "1",
            'instantly': 0.5,
            'daily': 3.7,
            'monthly': 317.3,
            'timestamp': int(datetime.datetime.now().timestamp())*1000,
            'message': f"this is the last measure of the solar panel: {test_id}"
        }

        assert expected == userViewmodel
