from src.shared.domain.entities.solar_panel import SolarPanel
from src.shared.domain.enums.state_enum import STATE


class MeasureSolarPanelViewmodel:
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
            'message': "the measure was created successfully"
        }
