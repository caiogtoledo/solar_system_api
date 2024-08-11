from src.shared.domain.entities.solar_panel import SolarPanel


class GetSolarPanelProductionViewmodel:
    solar_panel_id: str
    instantly: float
    daily: float
    monthly: float
    timestamp: int

    def __init__(self, solar_panel: SolarPanel):
        self.solar_panel_id = solar_panel.solar_panel_id
        self.instantly = solar_panel.instantly
        self.daily = solar_panel.daily
        self.monthly = solar_panel.monthly
        self.timestamp = solar_panel.timestamp

    def to_dict(self):
        return {
            'solar_panel_id': self.solar_panel_id,
            'instantly': self.instantly,
            'daily': self.daily,
            'monthly': self.monthly,
            'timestamp': self.timestamp,
            'message': f"this is the last measure of the solar panel: {self.solar_panel_id}"
        }
